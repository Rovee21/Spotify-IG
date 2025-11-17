import React from "react";

function Login(){
    const handleLogin = () => {
        window.location.href = "http://localhost:8000/login";
      };


      return (
        <div className="flex flex-col h-screen bg-black text-white">
          {/* Top-left title */}
          <div className="p-6">
            <h1 className="text-3xl font-extrabold tracking-wide">Resonate</h1>
          </div>
    
          {/* Center description */}
          <div className="flex-grow flex items-center justify-center">
            <p className="text-center text-2xl max-w-xl font-light opacity-90">
              Wanna have a social media platform to talk about music with your friends?  
              <span className="block mt-2 font-semibold">Look no further.</span>
            </p>
          </div>
    
          {/* Bottom login button */}
          <div className="flex items-center justify-center mb-12 space-x-4">
            <span className="text-lg">Login with Spotify</span>
            <button
              onClick={handleLogin}
              className="px-6 py-2 bg-green-500 hover:bg-green-600 transition rounded-lg font-semibold"
            >
              Continue
            </button>
          </div>
        </div>
      );
}

export default Login;