"use client"

import { Url } from "next/dist/shared/lib/router/router";
import { ReactNode } from "react";
import Link from "next/link";
import clsx, { ClassValue } from "clsx";
// import { usePathname } from "next/navigation";

interface NavbarLinkProps {
  children: ReactNode;
  href: Url;
  extraClassNames?: ClassValue;
}

export default function NavbarLink({children, href, extraClassNames}: NavbarLinkProps) {
  // const pathname = usePathname();

  return (
    <Link href={href} 
      className={clsx(
        "hover:text-text-primary-hover",
        "transition delay-50",
        // pathname === href ? "text-text-primary-hover": "",
        extraClassNames,
      )}
    >
      {children}
    </Link>
  );
}