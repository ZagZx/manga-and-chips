

import { MenuStatus } from "@/types/status";
import { faUserCircle } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import clsx from "clsx";


interface ProfileMenuProps {
  status: MenuStatus;
}

export default function ProfileMenu({ status }: ProfileMenuProps) {
  return(
    <>
      <FontAwesomeIcon className="w-7 cursor-pointer hover:text-primary" icon={faUserCircle}/> 
      <div 
        className={clsx(
          status === "open" ? "flex" : "hidden",
        )}
      >
        oi
      </div>
    </>    
  );
}