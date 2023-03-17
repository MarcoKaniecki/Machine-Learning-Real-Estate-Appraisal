import { useState, useEffect } from "react";
import axios from "axios";
import { BsImages, BsCardText } from 'react-icons/bs'

import supportImg from '../assets/appraisal-bg.png'

/* Toast is used to display a quick pop-up message for confirmation when the form is submitted */
const Toast = ({ message, duration = 3000, onClose }) => {
  const [show, setShow] = useState(true);

  useEffect(() => {
    const timer = setTimeout(() => {
      setShow(false);
      onClose();
    }, duration);

    return () => clearTimeout(timer);
  }, [duration, onClose]);

  /* set location of toast and how it should be displayed */
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


/* handle for containing appraisal information, uses axios to send data to backend database */
const Appraisal = () => {
  /* Consider setting default values for Demo purposes */
  const [image, setImage] = useState(null);
  const [zone, setZone] = useState("");
  const [lotArea, setLotArea] = useState("");

  /* combines data in the form and sends it as one package to backend */
  const handleSubmit = async (e) => {
    e.preventDefault();
    let formData = new FormData();
    formData.append("image", image);
    formData.append("zone", zone);
    formData.append("lotArea", lotArea);

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

  /* display toast */
  const handleShowToast = () => {
    setShowToast(true);
  };

  /* hide toast */
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
                  {/* image input */}
                  <input
                    type="file" required
                    id="image" accept="image/png, image/jpeg"
                    onChange={(e) => setImage(e.target.files[0])}
                    className="border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                  />
                </div>
              </div>
            </div>

            {/* area containing all feature inputs */}
            <div className='bg-white rounded-xl shadow-2xl'>
              <div className='p-8'>
                <BsCardText className='w-16 h-16 p-4 bg-indigo-600 text-white rounded-lg mt-[-4rem]'/>
                <h3 className='font-bold text-2xl my-6'>Text</h3>
                
                <div className="grid gap-6 mb-6 md:grid-cols-2">
                  
                  {/* Zone/Neighbourhood input field */}
                  <div>
                    <label for="zone" className="block mb-2 text-sm font-medium text-gray-900">Zone</label>
                    <select id="zone" type="text" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-indigo-600 focus:border-indigo-600 block w-full p-2.5 h-10" 
                    onChange={(e) => setZone(e.target.value)} required>
                      <option value="A">Agriculture</option>
                      <option value="C">Commercial</option>
                      <option value="FV">Floating Village Residential</option>
                      <option value="I">Industrial</option>
                      <option value="RH">Residential High Density</option>
                      <option value="RM">Residential Medium Density</option>
                      <option value="RL">Residential Low Density</option>
                      <option value="RP">Residential Low Density Park</option>
                    </select>
                  </div>

                  {/* Lot Area input field */}
                  <div>
                    <label className="block mb-2 text-sm font-medium text-gray-900">Lot Area in sqft</label>
                    {/* Step attribute set so only integers can be submitted */}
                    <input id="lotArea" type="number" step="1" min="0" max="1000000" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-indigo-600 focus:border-indigo-600 block w-full p-2.5" 
                    value={lotArea} onChange={(e) => setLotArea(e.target.value)} placeholder="1200" required />
                  </div>


                </div>
              </div>
            </div>
        
            {/* TODO: fix button so toast only shows when all fields are inputted and valid */}
            {/* Appraise button to submit form */}
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