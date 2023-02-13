import React, { useState } from 'react'

import { BsImages, BsCardText, BsSave, BsCloudUpload } from 'react-icons/bs'

import supportImg from '../assets/appraisal-bg.png'

const Appraisal = () => {
    const [description, setDescription] = useState('');

    const handleSubmit = async (event) => {
        event.preventDefault();
        try {
          const response = await fetch('/api/rawappraisaldata/', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify({ description })
          });
          if (!response.ok) {
            throw new Error('Network response was not ok');
          }
          setDescription('');
        } catch (error) {
          console.error('There was a problem submitting the form:', error);
        }
      };

    return (
        <div name='appraisal' className='w-full mt-24'>
            {/* the /90 after 900 for the color is for transparency */}
            <div className='w-full h-[700px] bg-gray-900/90 absolute'>
                <img className='w-full h-full object-cover mix-blend-overlay' src={supportImg} alt="/" />
            </div>

            <div className='max-w-[1240px] mx-auto text-white relative'>
                <div className='px-4 py-12'>
                    <h2 className='text-3xl pt-8 text-slate-300 uppercase text-center'>Appraisal</h2>
                    <h3 className='text-5xl fond-bold py-6 text-center'>Steps to get your home appraised</h3>
                    <p className='py-4 text-3xl text-slate-300 text-center'>Lorem ipsum dolor sit amet consectetur adipisicing elit. Nihil tempore recusandae, eos harum dolorum cupiditate commodi natus odit id a quo ut ea. Ipsum nemo facilis delectus repellendus. Eum, sit.</p>
                </div>
                
                {/* div for all boxes */}
                <div className='grid grid-cols-1 relative gap-x-8 gap-y-16 px-4 pt-12 sm:pt-20 text-black'>
                    {/* div for each separate box */}
                    <div className='bg-white rounded-xl shadow-2xl'>
                        <div className='p-8'>
                            <BsImages className='w-16 h-16 p-4 bg-indigo-600 text-white rounded-lg mt-[-4rem]'/>
                            <h3 className='font-bold text-2xl my-6'>Images</h3>

                            <div className="flex items-center justify-center w-full">
                                <label for="dropzone-file" className="flex flex-col items-center justify-center w-full h-64 border-2 border-gray-300 border-dashed rounded-lg cursor-pointer bg-gray-50 hover:bg-gray-100">
                                    <div className="flex flex-col items-center justify-center pt-5 pb-6">
                                        <BsCloudUpload className='w-8 h-8 text-indigo-600'/>
                                        <p className="mb-2 text-sm text-gray-600"><span className="font-semibold">Click to upload</span> or drag and drop</p>
                                        <p className="text-xs text-gray-600">PNG or JPG (MAX. 800x400px)</p>
                                    </div>
                                    {/* add required multiple in the future */}
                                    <input id="dropzone-file" type="file" className="hidden" />
                                </label>
                            </div> 

                        </div>
                        <div className='bg-slate-100 pl-8 py-4 rounded-b-xl'>
                            <p className='flex items-center text-indigo-600'>
                                Save <BsSave className='w-5 ml-2' />
                            </p>
                        </div>
                    </div>


                    <div className='bg-white rounded-xl shadow-2xl'>
                        <div className='p-8'>
                            <BsCardText className='w-16 h-16 p-4 bg-indigo-600 text-white rounded-lg mt-[-4rem]'/>
                            <h3 className='font-bold text-2xl my-6'>Text</h3>

                            {/*
                            <form>
                                <div className="grid gap-6 mb-6 md:grid-cols-2">
                                    <div>
                                        <label className="block mb-2 text-sm font-medium text-gray-900">Number of beds</label>
                                        <input type="number" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-indigo-600 focus:border-indigo-600 block w-full p-2.5" placeholder="3" required />
                                    </div>
                                    <div>
                                        <label className="block mb-2 text-sm font-medium text-gray-900">Number of baths</label>
                                        <input type="number" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-indigo-600 focus:border-indigo-600 block w-full p-2.5" placeholder="2" required />
                                    </div>
                                    <div>
                                        <label className="block mb-2 text-sm font-medium text-gray-900">Build year</label>
                                        <input className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-indigo-600 focus:border-indigo-600 block w-full p-2.5" placeholder="2006" required />
                                    </div>  
                                    <div>
                                        <label className="block mb-2 text-sm font-medium text-gray-900">Size (sqft)</label>
                                        <input className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-indigo-600 focus:border-indigo-600 block w-full p-2.5" placeholder="3915" required />
                                    </div>
                                    <div>
                                        <label className="block mb-2 text-sm font-medium text-gray-900">Property Type</label>
                                        <input className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-indigo-600 focus:border-indigo-600 block w-full p-2.5" placeholder="House" required />
                                    </div>
                                    <div>
                                        <label className="block mb-2 text-sm font-medium text-gray-900">Something Else</label>
                                        <input type="number" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-indigo-600 focus:border-indigo-600 block w-full p-2.5" placeholder="" required />
                                    </div>
                                </div>
                                <div className="mb-6">
                                    <label className="block mb-2 text-sm font-medium text-gray-900">Something Longer</label>
                                    <input className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-indigo-600 focus:border-indigo-600 block w-full p-2.5" placeholder="" required />
                                </div> 
                            </form>
                            */}
                            <form onSubmit={handleSubmit}>
                                <textarea id="message" 
                                value={description}
                                onChange={event => setDescription(event.target.value)}
                                rows="4" 
                                className="block p-2.5 w-full text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-indigo-600 focus:border-indigo-600" 
                                placeholder="Detailed description of home...">
                                </textarea>
                            </form>
                        </div>

                        {/* 
                            Pressing save will already have the text running through the NLP, to extract the info.
                            If anything is missing something will pop-up saying whats missing.
                            Only after the bare minimum is accounted for, will the appraise button actually work.
                        */}

                        <div className='bg-slate-100 pl-8 py-4 rounded-b-xl'>
                            <p className='flex items-center text-indigo-600'>
                                Save <BsSave className='w-5 ml-2' />
                            </p>
                        </div>
                    </div>

                    <div className='text-center'>
                        <button type="submit" className='py-3 px-6 sm:w-[60%] md:w-[30%] my-4 shadow-xl'>Appraise!</button>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default Appraisal