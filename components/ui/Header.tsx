import { faBookOpen } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import Link from "next/link";
import clsx from "clsx";
import NavbarLink from "./NavbarLink";
import Icon from "./Icon";

export default function Header() {
  return (
    <header className="bg-skeleton flex justify-around py-4 shadow-xl">
      <Link href="/">
        <Icon />
      </Link>
      <nav className="flex gap-3">
        <NavbarLink href="/">Início</NavbarLink>
        <NavbarLink href="#">Biblioteca</NavbarLink>
        <NavbarLink href="#">Categorias</NavbarLink>
      </nav>
    </header>
  );
}
