import Navbar from "./components/ Navbar";
import './HomePage.css';
import Footer from "./components/Footer";
function HomePage(){

    return (
        <div className="HomePage">
            <Navbar/>
            <div  className="ad">
                <div className="ad-content"></div>
            </div>

            <div className="New-Release sub-sections">
                <h1>New Releases Movies</h1>
            </div>

            <div className="popular-movies sub-sections">
                <h1>Popular Movies</h1>
            </div>
            
            <div className="sub-sections">
                <h1>Recommended Movies</h1>
            </div>

            <div className="sub-sections">
                <h1>Some Classics</h1>
            </div>
            <Footer/>
        </div>
    )
}

export default HomePage
