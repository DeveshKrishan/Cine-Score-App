import Select from 'react-select';
import movieTitleJSON from "./movie_title.json";

interface Movie {
    value: string;
    label: string
}

interface movieTitleData {
    [key: string]: string[];
}

function HomePage(){
    const movieTitleData: movieTitleData= movieTitleJSON;

    const options: Movie[] = Object.keys(movieTitleData).map((key) => ({
        "value": key,
        "label": movieTitleData[key][0]
    }))

    return (
        <>
            <Select options={options}/>
            <p>Select is laggy af because it loads all 22k movie into the select option. Will crash if click it.</p>
        </>
    )
}

export default HomePage
