import logo from "../images/menu.png/"
import Select from 'react-select';

function Navbar(){
    const options = [
        { value: 'chocolate', label: 'Chocolate' },
        { value: 'strawberry', label: 'Strawberry' },
        { value: 'vanilla', label: 'Vanilla' }
      ]

    return (
            <div className="grid gap-10 grid-cols-[1.25fr_2fr_1fr] grid-rows-1 items-center p-3 bg-navbar">
                <h1 className="text-[2.5vw] font-bold col-span-1">Movie Rating App</h1>
                <Select options={options} className="col-start-2 col-end-3"/>
                <div className="bg-white rounded-full p-3 col-start-3 col-end-4 max-w-fit justify-self-end">
                    <img src={logo} className="w-10" alt="logo"/>
                </div>
            </div>
    )
}

export default Navbar
