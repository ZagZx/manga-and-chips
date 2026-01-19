import Button from "@/components/ui/Button";

export default function Home() {
  return (
    <>
      <div className="w-50 h-50 flex flex-col bg-background gap-3">
        <Button>Primário</Button>
        <Button style="secondary">Secundário</Button>
      </div>
    </>
  );
}
