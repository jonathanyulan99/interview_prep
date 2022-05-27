import React from "react";
import "./header.css";
import CTA from "./CTA";
import ME from "../../assets/adrain_header_image.jpg";
import HeaderSocials from "./HeaderSocials";

const Header = () => {
  return (
    <header>
      <div className="container header_container">
        <h5>Hello My Name Is</h5>
        <h1>VahnStrife</h1>
        <h5 className="text-light">
          I Am A Gaming, Life Enthusiast, Working Towards Pro-Status
        </h5>

        <CTA />
        <HeaderSocials />

        <div className="me">
          <img className="img-header-photo" src={ME} alt="me" />
        </div>

        <a href="#contact" className="scroll_down">
          Scroll Down
        </a>
      </div>
    </header>
  );
};

export default Header;
