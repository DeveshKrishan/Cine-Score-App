import logo from "../images/menu.png";
import { TextInput } from "@tremor/react";
import { SearchIcon } from "@heroicons/react/solid";

function Navbar(){

    return (
            <div className="grid gap-10 grid-cols-[1.25fr_2fr_1fr] grid-rows-1 items-center p-3 bg-navbar">
                <h1 className="text-[2.5vw] font-bold col-span-1">Movie Rating App</h1>
                <>
                <TextInput icon={SearchIcon} className="bg-white" placeholder="Search..." />
                </>
                <div className="bg-white rounded-full p-3 col-start-3 col-end-4 max-w-fit justify-self-end">
                    <img src={logo} className="w-10" alt="logo"/>
                </div>
            </div>
    )
}

export default Navbar
