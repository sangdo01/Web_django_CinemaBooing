// import icon fontaweome
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faFacebook, faInstagram, faTwitter, faLinkedinIn, faYoutube } from "@fortawesome/free-brands-svg-icons"


import cong_thuong_img from './../../assets/img/cong-thuong.png';


const Footer = () => {
    return (
        <>
            {/* <!-- Footer Start --> */}
            <div className="container-fluid bg-dark pt-5 px-sm-3 px-md-5 mt-5">
                <div className="row py-4">
                    <div className="col-lg-3 col-md-6 mb-5">
                        <h5 className="mb-4 text-white text-uppercase font-weight-bold">Chăm sóc khách hàng</h5>
                        <p className="font-weight-medium"><i className="fa fa-map-marker-alt mr-2"></i>### Lê Văn Việt, Thủ Đức</p>
                        <p className="font-weight-medium"><i className="fa fa-phone-alt mr-2"></i>+### ### ###</p>
                        <p className="font-weight-medium"><i className="fa fa-envelope mr-2"></i>dscinema@gmail.com</p>
                        <h6 className="mt-4 mb-3 text-white text-uppercase font-weight-bold">Kết nối với chúng tôi</h6>

                    </div>
                    <div className="col-lg-3 col-md-6 mb-5">
                        <h5 className="mb-4 text-white text-uppercase font-weight-bold">DS Cinema</h5>
                        <a href="#" style={{ color: "#9A9DA2" }}><p className="font-weight-medium">Về chúng tôi</p></a>
                        <a href="{% url 'contact' %}" style={{ color: "#9A9DA2" }}><p className="font-weight-medium">Liên hệ</p></a>

                    </div>
                    <div className="col-lg-3 col-md-6 mb-5">
                        <h5 className="mb-4 text-white text-uppercase font-weight-bold">Điều khoản sử dụng</h5>
                        <a href="#" style={{ color: "#9A9DA2" }}><p className="font-weight-medium">Chính sách bảo mật</p></a>
                        <a href="#" style={{ color: "#9A9DA2" }}><p className="font-weight-medium">Chính sách thanh toán</p></a>
                    </div>
                    <div className="col-lg-3 col-md-6 mb-5">
                        <h5 className="mb-4 text-white text-uppercase font-weight-bold">Kết nối với chúng tôi</h5>
                        <div className="d-flex justify-content-start">
                            <a className="btn btn-lg btn-secondary btn-lg-square mr-2" href="#"><FontAwesomeIcon className="fab fa-twitter" icon={faTwitter} /></a>
                            <a className="btn btn-lg btn-secondary btn-lg-square mr-2" href="#"><FontAwesomeIcon className="fab fa-facebook- f" icon={faFacebook} /></a>
                            <a className="btn btn-lg btn-secondary btn-lg-square mr-2" href="#"><FontAwesomeIcon className="fab fa-linkedin-in" icon={faLinkedinIn} /></a>
                            <a className="btn btn-lg btn-secondary btn-lg-square mr-2" href="#"><FontAwesomeIcon className="fab fa-instagram" icon={faInstagram} /></a>
                            <a className="btn btn-lg btn-secondary btn-lg-square" href="#"><FontAwesomeIcon className="fab fa-youtube" icon={faYoutube} /></a>
                        </div>
                        <br />
                        <img src={cong_thuong_img} alt="anh_bo_cong_thuong" />
                    </div>

                </div>
            </div>
            <div className="container-fluid py-4 px-sm-3 px-md-5" style={{ background: "#111111" }}>
                <p className="m-0 text-center">&copy; <a href="#">DSCinema - 19DTHA1</a>. All Rights Reserved.
                    Design by <a href="#">DVS</a></p>
            </div>
            {/* <!-- Footer End --> */}
        </>
    )
}

export default Footer;