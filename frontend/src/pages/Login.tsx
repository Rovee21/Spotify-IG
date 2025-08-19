import React from "react";

function Login(){
    const handleLogin = () => {
        window.location.href = "http://localhost:8000/login";
      };


    return(
        <div className="flex flex-col items-center justify-center h-screen">
            <h1 className="text-xl font-bold">Spotify Login</h1>
            <button
            onClick={handleLogin}
            className="mt-4 px-6 py-2 bg-green-500 text-white rounded-lg"
            >
            Login with Spotify
            </button>
        </div>
    );
}

export default Login;