import { faBookOpen } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";

export default function Header() {
  return (
    <header className="bg-big-stone-950">
      <div className="flex align-middle justify-center">
        <FontAwesomeIcon icon={faBookOpen} className="text-red-500 w-6" />
        <span>
          Manga
          <span className="text-red-500">&</span>
          Chips
        </span>
      </div>
    </header>
  );
}
