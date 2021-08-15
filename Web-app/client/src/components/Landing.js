import './Landing.css';
import { useState } from 'react';

function Landing() {
    const [formData, setFormData] = useState();

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value.trim() });
    };

    const handleSubmit = (e) => {
        e.preventDefault()
        //console.log(formData);
        /*
        const addRequest = async () => {
            const response = await axios.get(API_url + `/add/${formData['keyword-input']}/${formData['since-input']}/${formData['quantity-input']}`);
            apiRequest();
        };*/
    };

    return (
        <>

        </>
    );
}

export default Landing;