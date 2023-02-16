import { useState, useEffect } from "react";
import axios from "axios";
import { BsImages, BsCardText } from 'react-icons/bs'

import supportImg from '../assets/appraisal-bg.png'


const Toast = ({ message, duration = 3000, onClose }) => {
  const [show, setShow] = useState(true);

  useEffect(() => {
    const timer = setTimeout(() => {
      setShow(false);
      onClose();
    }, duration);

    return () => clearTimeout(timer);
  }, [duration, onClose]);

  return (
    <div
      className={`fixed bottom-0 right-0 p-4 m-4 rounded-md bg-gray-700 text-white transition-opacity duration-500 ${
        show ? "opacity-100" : "opacity-0"
      }`}
    >
      {message}
    </div>
  );
}



const Appraisal = () => {
  const [image, setImage] = useState(null);
  const [content, setContent] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    let formData = new FormData();
    formData.append("image", image);
    formData.append("content", content);
    try {
      await axios.post("http://localhost:8000/api/posts/", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });
    } catch (error) {
      console.log(error);
    }
  };


  const [showToast, setShowToast] = useState(false);

  const handleShowToast = () => {
    setShowToast(true);
  };

  const handleHideToast = () => {
    setShowToast(false);
  };

  return (
    <form onSubmit={handleSubmit}>

      <div name='appraisal' className='w-full mt-24'>
        
        <div className='w-full h-[700px] bg-gray-900/90 absolute'>
          <img className='w-full h-full object-cover mix-blend-overlay' src={supportImg} alt="/" />
        </div>

        <div className='max-w-[1240px] mx-auto text-white relative'>
          
          <div className='px-4 py-12'>
            <h2 className='text-3xl pt-8 text-slate-300 uppercase text-center'>Appraisal</h2>
            <h3 className='text-5xl fond-bold py-6 text-center'>Steps to get your home appraised</h3>
            <p className='py-4 text-3xl text-slate-300 text-center'>Lorem ipsum dolor sit amet consectetur adipisicing elit. Nihil tempore recusandae, eos harum dolorum cupiditate commodi natus odit id a quo ut ea. Ipsum nemo facilis delectus repellendus. Eum, sit.</p>
          </div>
        
          <div className='grid grid-cols-1 relative gap-x-8 gap-y-16 px-4 pt-12 sm:pt-10 text-black'>
            
            {/* div for each separate box */}
            <div className='bg-white rounded-xl shadow-2xl'>
              
              <div className='p-8'>
                <BsImages className='w-16 h-16 p-4 bg-indigo-600 text-white rounded-lg mt-[-4rem]'/>
                <h3 className='font-bold text-2xl my-6'>Images</h3>
                <div className="flex items-center justify-center w-full">
                  <input
                    type="file" required
                    id="image" accept="image/png, image/jpeg"
                    onChange={(e) => setImage(e.target.files[0])}
                    className="border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                  />
                </div>
              </div>
            </div>

            <div className='bg-white rounded-xl shadow-2xl'>
              <div className='p-8'>
                <BsCardText className='w-16 h-16 p-4 bg-indigo-600 text-white rounded-lg mt-[-4rem]'/>
                <h3 className='font-bold text-2xl my-6'>Text</h3>
                <textarea
                  id="content"
                  value={content} required placeholder="Enter detailed description of home..."
                  onChange={(e) => setContent(e.target.value)}
                  className="border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                ></textarea>
              </div>
            </div>
        
            {/* Appraise button */}
            <div className='text-center'>
              <input
                type="submit"
                value="Appraise!" onClick={handleShowToast}
                className="py-3 px-6 sm:w-[60%] md:w-[30%] my-4 shadow-xl text-white border bg-indigo-600 border-indigo-600
                hover:bg-transparent hover:text-indigo-600 rounded-md cursor-pointer"
              />
              {showToast && (
              <Toast message="Form submitted!" duration={3000} onClose={handleHideToast} />
              )}
            </div>
          </div>
        </div>
      </div>
    </form>
  );
}

export default Appraisal