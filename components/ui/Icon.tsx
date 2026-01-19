import { faBookOpen } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";

export default function Icon() {
  return(
    <div className="flex gap-1 text-lg align-middle justify-center font-bold">
      <FontAwesomeIcon icon={faBookOpen} className="text-primary w-6" />
      <span>
        Manga
        <span className="text-primary">&</span>
        Chips
      </span>
    </div>
  );
}