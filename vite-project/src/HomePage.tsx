import Navbar from "./components/ Navbar";
import './HomePage.css';
function HomePage(){

    return (
        <div className="HomePage">
            <Navbar/>
            <div  className="ad">
                <div className="ad-content"></div>
            </div>

            <div className="New-Release">
                <h1>New Releases Movies</h1>
            </div>
        </div>
    )
}

export default HomePage
