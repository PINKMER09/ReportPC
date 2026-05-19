import streamlit as st
import streamlit.components.v1 as components

# 1. CẤU HÌNH TRANG WEB
st.set_page_config(page_title="Cổng Báo Cáo Nội Bộ", page_icon="🏥", layout="wide")

# 2. DANH SÁCH TÀI KHOẢN HỢP LỆ
USERS = {
    "admin": "phuongchau3080",
    "PC-00645": "phuongchau",
    "PC-01817": "phuongchau",
    "PC-20139": "phuongchau",
    "PC-10222": "phuongchau"
}

# 3. KHỞI TẠO BIẾN TRẠNG THÁI
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'username' not in st.session_state:
    st.session_state['username'] = ""

# 4. GIAO DIỆN MÀN HÌNH ĐĂNG NHẬP
def login_screen():
    col1, col2, col3 = st.columns([1, 1.2, 1])
    
    with col2:
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        st.markdown(
            """
            <div style='text-align: center;'>
                <h2 style='color: #8b008b;'>🏥 BÁO CÁO CHỈ SỐ<br>ĐIỀU DƯỠNG</h2>
            </div>
            """, 
            unsafe_allow_html=True
        )
        st.markdown("<p style='text-align: center; color: gray;'>Vui lòng xác thực để truy cập dữ liệu nội bộ</p>", unsafe_allow_html=True)
        
        with st.form("login_form"):
            username = st.text_input("👤 Tên đăng nhập")
            password = st.text_input("🔑 Mật khẩu", type="password")
            submitted = st.form_submit_button("Đăng Nhập", use_container_width=True)
            
            if submitted:
                if username in USERS and USERS[username] == password:
                    st.session_state['logged_in'] = True
                    st.session_state['username'] = username
                    st.rerun() 
                else:
                    st.error("❌ Sai tên đăng nhập hoặc mật khẩu!")

# 5. GIAO DIỆN MÀN HÌNH BÁO CÁO (Sau khi đăng nhập)
def dashboard_screen():
    header_col1, header_col2 = st.columns([4, 1])
    with header_col1:
        st.subheader(f"Xin chào, {st.session_state['username']} 👋")
    with header_col2:
        if st.button("🚪 Đăng xuất", use_container_width=True):
            st.session_state['logged_in'] = False
            st.session_state['username'] = ""
            st.rerun()

    # KHU VỰC CẬP NHẬT NGUYÊN NHÂN & HÀNH ĐỘNG KHI TRỄ TIẾN ĐỘ
    st.markdown("---")
    with st.expander("📝 Cập nhật nguyên nhân trễ tiến độ dự án (Nếu có)", expanded=False):
        c_col1, c_col2 = st.columns(2)
        with c_col1:
            project_name = st.selectbox("Chọn dự án", ["Dự án AP Automation", "Dự án Cải tiến Điều dưỡng", "Khác..."])
            cause = st.text_area("🔴 Nguyên nhân trễ (Cause)", placeholder="Nhập lý do cụ thể tại đây...")
        with c_col2:
            status = st.select_slider("Mức độ trễ", options=["Bình thường", "Trễ nhẹ", "Trễ nghiêm trọng"])
            action = st.text_area("🟢 Hành động khắc phục (Action)", placeholder="Các bước sẽ thực hiện để kịp tiến độ...")
        
        if st.button("Gửi báo cáo cập nhật", use_container_width=True):
            if cause and action:
                st.success(f"✅ Đã ghi nhận báo cáo trễ tiến độ cho {project_name}!")
            else:
                st.warning("⚠️ Vui lòng điền đầy đủ cả Nguyên nhân và Hành động.")

    st.markdown("---")
    
    # ĐƯỜNG LINK POWER BI
    POWER_BI_URL = "https://app.powerbi.com/view?r=eyJrIjoiN2Q2YWExNGItZTBjZi00YjIxLTk4MWUtNjA3ZTliODIyZjVmIiwidCI6IjhiZDRiMTQ5LTdmODItNDY3Ny1iNDQzLWQyNDk3NWRkOTAzMCIsImMiOjEwfQ%3D%3D"

    iframe_html = f"""
        <div style="display: flex; justify-content: center; align-items: center; width: 100%;">
            <iframe title="Báo Cáo Power BI" 
                    width="100%" 
                    height="850px" 
                    src="{POWER_BI_URL}" 
                    frameborder="0" 
                    allowFullScreen="true"
                    style="border-radius: 8px; box-shadow: 0px 4px 12px rgba(0,0,0,0.1);">
            </iframe>
        </div>
    """
    components.html(iframe_html, height=880)

# 6. BỘ ĐIỀU CHUYỂN LOGIC TỔNG
if not st.session_state['logged_in']:
    login_screen()
else:
    dashboard_screen()
