import React from "react";
//import FILENAME_VARIABLE from '../../ or ./ or ../' depending where it is located
//you can then grab that and utilize i t in our returning of our components
// <a href={FILENMAE_VARIABLE} download>TEXT THAT SHOWS AS LINK </a>
// Destructuring the imported .pdf or file from another folder

const CTA = () => {
  return (
    <div className="cta">
      <a href="https://www.twitch.tv/vahnstrife" className="btn">
        Check Out My Twitch!
      </a>
      <a href="#contact" className="btn btn-primary">
        Let's Connect!
      </a>
    </div>
  );
};

export default CTA;
