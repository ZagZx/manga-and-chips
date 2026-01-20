
import { faGithub, faLinkedin } from "@fortawesome/free-brands-svg-icons";
import mangadex from "@/public/assets/mangadex.png"
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import NavbarLink from "./NavbarLink";

export default function Footer() {
  return(
    <footer className="bg-skeleton flex justify-center relative py-12 items-center">
      <div className="flex gap-1 items-center justify-center">
        <span>Powered by Mangadex API</span>
        <img className="w-5 h-5" src={mangadex.src}/>
      </div>
      <nav className="flex flex-col gap-1 absolute right-20">
        <NavbarLink href="https://github.com/ZagZx" target="_blank">
          <FontAwesomeIcon className="w-4" icon={faGithub}/>
          Github
        </NavbarLink>
        <NavbarLink href="https://www.linkedin.com/in/pedro-victor-75a069363/" target="_blank">
          <FontAwesomeIcon className="w-4" icon={faLinkedin}/>
          Linkedin
        </NavbarLink>
      </nav>
    </footer>
  );
}