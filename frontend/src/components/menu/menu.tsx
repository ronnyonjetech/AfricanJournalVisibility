import MenuItem from "@/components/menu/menu-item";

const MENU_ITEMS = [
  { name: "Home", to: "/" },
  { name: "Reach Out", to: "/contact" },
  { name: "Who We Are", to: "/about" },
  { name: "Resources", to: "/resources" },
  { name: "Need Help?", to: "/support" },
];

function Menu({ className }: { className?: string }) {
  return (
    //Gve custom color
    <ul className={className} style={{ color: "red", fontSize: "14px" }}>
      {MENU_ITEMS.map((link) => (
        <MenuItem key={link.name} to={link.to} name={link.name} />
      ))}
    </ul>
  );
}

export default Menu;
