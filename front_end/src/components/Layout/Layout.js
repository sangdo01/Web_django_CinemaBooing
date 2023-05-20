import Topbar from "./Topbar";
import Navigation from "./Navigation";
import Footer from "./Footer";

import './../../assets/css/style.css'

const Layout = ({ children }) => {
    return (
        <>         
            <Topbar />
            <Navigation />
            <div>{children}</div>
            <Footer />
        </>
    )
}

export default Layout;