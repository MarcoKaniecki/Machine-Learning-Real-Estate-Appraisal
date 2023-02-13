import React, { Component } from 'react'
import axios from 'axios'

import { BsImages, BsCardText, BsSave, BsCloudUpload } from 'react-icons/bs'

import supportImg from '../assets/appraisal-bg.png'


class Appraisal extends Component {
    state = {
        content: '',
        image: null
    };

    handleChange = (e) => {
        this.setState({
            [e.target.id]: e.target.value
        })
    };

    handleImageChange = (e) => {
        this.setState({
          image: e.target.files[0]
        })
    };

    handleSubmit = (e) => {
        e.preventDefault();
        console.log(this.state);
        let form_data = new FormData();
        form_data.append('image', this.state.image, this.state.image.name);
        form_data.append('content', this.state.content);
        let url = 'http://localhost:8000/api/appraisal/';
        axios.post(url, form_data, {
          headers: {
            'content-type': 'multipart/form-data'
          }
        })
        .then(res => {
            console.log(res.data);
        })
        .catch(err => console.log(err))
    };
    
    render() {
        return (
            <div>
                <form onSubmit={this.handleSubmit}>
                <p>
                    <input type="text" placeholder='Content' id='content' value={this.state.content} onChange={this.handleChange} required/>

                </p>
                <p>
                    <input type="file"
                        id="image"
                        accept="image/png, image/jpeg"  onChange={this.handleImageChange} required/>
                </p>
                <input type="submit"/>
                </form>
            </div>
        )
    }

}

export default Appraisal;