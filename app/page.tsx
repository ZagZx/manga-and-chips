import Button from "@/components/ui/Button";
import Header from "@/components/ui/Header";

export default function Home() {
  return (
    <>
      <Header />
      <div className="w-50 h-50 flex flex-col bg-black gap-3">
        <Button>Primário</Button>
        <Button style="secondary">Secundário</Button>
      </div>
    </>
  );
}
