// "use client"

import { Url } from "next/dist/shared/lib/router/router";
import { HTMLAttributeAnchorTarget, ReactNode } from "react";
import Link from "next/link";
import clsx, { ClassValue } from "clsx";
// import { usePathname } from "next/navigation";

interface NavbarLinkProps {
  children: ReactNode;
  href: Url;
  target?: HTMLAttributeAnchorTarget;
  extraClassNames?: ClassValue;
}

export default function NavbarLink({children, href, target, extraClassNames}: NavbarLinkProps) {
  // const pathname = usePathname();

  return (
    <Link href={href} 
      className={clsx(
        "hover:text-primary",
        "transition delay-50",
        "flex gap-1",
        // pathname === href ? "text-text-primary-hover": "",
        extraClassNames,
      )}
      target={target}
    >
      {children}
    </Link>
  );
}