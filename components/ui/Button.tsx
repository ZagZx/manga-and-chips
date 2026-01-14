import { ReactNode } from "react";

interface ButtonProps {
  children: ReactNode;
}

export default function Button({ children }: ButtonProps) {
  return(
    <button className="
      bg-primary-400 
      text-white font-bold 
      hover:bg-primary-600 hover:cursor-pointer
      rounded-2xl py-2">
      {children}
    </button>
  );
}