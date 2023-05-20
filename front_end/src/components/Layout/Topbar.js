const Topbar = () => {
    return (
        <>
            {/* <!-- Topbar Start --> */}
            <div className="container-fluid d-none d-lg-block">

                <div className="row align-items-center bg-white py-3 px-lg-5">
                    <div className="col-lg-4">
                        <a href="{% url 'home' %}" className="navbar-brand p-0 d-none d-lg-block">
                            <h1 className="m-0 display-4 text-uppercase text-primary">DS<span className="text-secondary font-weight-normal">Cinema</span></h1>
                        </a>
                    </div>
                    <div className="col-lg-8 text-center text-lg-right">

                    </div>
                </div>
            </div>
            {/* <!-- Topbar End --> */}
        </>
    )
}

export default Topbar