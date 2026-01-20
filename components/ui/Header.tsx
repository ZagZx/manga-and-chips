"use client"

// import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import Link from "next/link";
// import clsx from "clsx";
import NavbarLink from "./NavbarLink";
import Icon from "./Icon";
import ProfileMenu from "./ProfileMenu";
import { useState } from "react";
import { MenuStatus } from "@/types/status";

export default function Header() {
  const [menuStatus, setMenuStatus] = useState<MenuStatus>("closed");

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
      <div>
        <ProfileMenu status={menuStatus}/>
      </div>
    </header>
  );
}
