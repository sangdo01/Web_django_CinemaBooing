const Navigation = () => {
    return (
        <>

            {/* <!-- Navbar Start --> */}
            <div className="container-fluid p-0">
                <nav className="navbar navbar-expand-lg bg-dark navbar-dark py-2 py-lg-0 px-lg-5">
                    <div className="collapse navbar-collapse justify-content-between px-0 px-lg-3" id="navbarCollapse">
                        <div className="navbar-nav mr-auto py-0">
                            <a href="{% url 'home' %}" className="nav-item nav-link active">Trang chủ</a>
                            <div className="nav-item dropdown">
                                <a href="#" className="nav-link dropdown-toggle" data-toggle="dropdown">Phim</a>
                                <div className="dropdown-menu rounded-0 m-0">
                                    <a href="{% url 'nowshowing' %}" className="dropdown-item">Đang chiếu</a>
                                    <a href="{% url 'comingsoon' %}" className="dropdown-item">Sắp chiếu</a>
                                </div>
                            </div>

                            <div className="nav-item dropdown">
                                <a href="#" className="nav-link dropdown-toggle" data-toggle="dropdown">Thông tin</a>
                                <div className="dropdown-menu rounded-0 m-0">
                                    <a href="{% url 'about' %}" className="dropdown-item">Về chúng tôi</a>
                                    <a href="{% url 'directors' %}" className="dropdown-item">Đạo diễn</a>
                                    <a href="{% url 'actor' %}" className="dropdown-item">Diễn viên</a>
                                </div>
                            </div>

                            <a href="{% url 'news' %}" className="nav-item nav-link">Sự kiên</a>
                            <a href="{% url 'contact' %}" className="nav-item nav-link">Liên hệ</a>

                            {/* {% if request.user.is_authenticated %} */}
                            <div className="nav-item dropdown">
                                <a href="#" className="nav-link dropdown-toggle" data-toggle="dropdown">user name</a>
                                <div className="dropdown-menu rounded-0 m-0">
                                    <a href="#" className="dropdown-item">Tài khoản</a>
                                    <a href="{% url 'logout' %}" className="dropdown-item">Đăng xuất</a>
                                </div>
                            </div>
                            {/* {% else %} */}
                            <a href="{% url 'login' %}" className="nav-item nav-link">Đăng nhập</a>
                            {/* {% endif %} */}


                        </div>
                        <form action="{% url 'search' %}" method="POST">
                            <div className="input-group ml-auto d-none d-lg-flex" style={{width: "500px"}}>
                                <input type="text" className="form-control border-0" placeholder="Nhập tên phim ..." name="search"/>
                                    <div className="input-group-append">
                                        <button type="submit" className="input-group-text bg-primary text-dark border-0 px-3"><i
                                            className="fa fa-search"></i></button>
                                    </div>
                            </div>
                        </form>
                    </div>
                </nav>
            </div>
            {/* Navbar End */}
        </>
    )
}

export default Navigation;