import React from "react";
//target="blank" opens in a new page
import { IoLogoTwitch } from "react-icons/io";
import { SiFacebookgaming } from "react-icons/si";
import { TiSocialInstagram } from "react-icons/ti";
import { SiPatreon } from "react-icons/si";

const HeaderSocials = () => {
  return (
    <div className="header_socials">
      <a href="https://patreon.com" target="_blank" rel="noreferrer">
        <SiPatreon />
      </a>
      <a href="https://instagram.com" target="_blank" rel="noreferrer">
        <TiSocialInstagram />
      </a>
      <a href="https://twitch.com" target="_blank" rel="noreferrer">
        <IoLogoTwitch />
      </a>
      <a href="https://facebook.com" target="_blank" rel="noreferrer">
        <SiFacebookgaming />
      </a>
    </div>
  );
};

export default HeaderSocials;
