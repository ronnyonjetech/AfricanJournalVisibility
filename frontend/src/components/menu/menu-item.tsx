import { NavLink } from "react-router-dom";

function MenuItem({ name, to }: { name: string; to: string }) {
  return (
    <li>
      <NavLink
        className={({ isActive }) =>
          isActive ? "border-b font-bold text-navy" : "text-navy hover:border-b"
        }
        to={to}
        style={{ color: "#001F3F" }}
      >
        {name}
      </NavLink>
    </li>
  );
}

export default MenuItem;
