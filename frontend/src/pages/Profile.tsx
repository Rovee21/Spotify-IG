import React from "react";
import { useLocation } from "react-router-dom";

function Profile() {
  const location = useLocation();
  const params = new URLSearchParams(location.search);

  const name = params.get("name");
  const image = params.get("image");

  if (!name) {
    return <p>Loading profile...</p>;
  }

  return (
    <div className="flex flex-col items-center p-6">
        {image && (
        <img
            src={image}
            alt="Profile"
            className="w-24 h-24 rounded-full mb-4"
        />
        )}
        <h2 className="text-lg font-semibold">{name}</h2>
    </div>
  );
}

export default Profile;