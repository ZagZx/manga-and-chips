import clsx, { ClassValue } from "clsx";
import React, { ButtonHTMLAttributes, ReactNode } from "react";

type ButtonStyle = "primary" | "secondary"

interface ButtonProps {
  children: ReactNode;
  style?: ButtonStyle;
  extraClassNames?: ClassValue;
}

export default function Button({ children, style="primary", extraClassNames  }: ButtonProps) {
  return(
    <button className={clsx(
      "hover:cursor-pointer",
      "rounded py-2",
      "font-bold",
      "border-2",
      style === "primary" ? ("bg-primary hover:bg-primary-hover text-secondary border-transparent") : null,
      style === "secondary" ? ("bg-secondary hover:bg-secondary-hover text-primary border-primary  hover:border-primary-hover") : null,
      extraClassNames,
      )}
    >
      {children}
    </button>
  );
}