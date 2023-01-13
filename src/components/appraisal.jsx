import React from 'react'

import {BsImages, BsCardText, BsSave} from 'react-icons/bs'

import supportImg from '../assets/appraisal-bg.png'

const Appraisal = () => {
    return (
        <div className='w-full mt-24'>
            {/* the /90 after 900 for the color is for transparency */}
            <div className='w-full h-[700px] bg-gray-900/90 absolute'>
                <img className='w-full h-full object-cover mix-blend-overlay' src={supportImg} alt="/" />
            </div>

            <div className='max-w-[1240px] mx-auto text-white relative'>
                <div className='px-4 py-12'>
                    <h2 className='text-3xl pt-8 text-slate-300 uppercase text-center'>Appraisal</h2>
                    <h3 className='text-5xl fond-bold py-6 text-center'>Steps to get your home appraised</h3>
                    <p className='py-4 text-3xl text-slate-300'>Lorem ipsum dolor sit amet consectetur adipisicing elit. Nihil tempore recusandae, eos harum dolorum cupiditate commodi natus odit id a quo ut ea. Ipsum nemo facilis delectus repellendus. Eum, sit.</p>
                </div>
                
                {/* div for all boxes */}
                <div className='grid grid-cols-1 lg:grid-cols-2 relative gap-x-8 gap-y-16 px-4 pt-12 sm:pt-20 text-black'>
                    {/* div for each separate box */}
                    <div className='bg-white rounded-xl shadow-2xl'>
                        <div className='p-8'>
                            <BsImages className='w-16 h-16 p-4 bg-indigo-600 text-white rounded-lg mt-[-4rem]'/>
                            <h3 className='font-bold text-2xl my-6'>Images</h3>
                            <p className='text-gray-600 text-xl'>here we add the box to add images</p>
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
                            <p className='text-gray-600 text-xl'>here we add the box to add text</p>
                        </div>
                        <div className='bg-slate-100 pl-8 py-4 rounded-b-xl'>
                            <p className='flex items-center text-indigo-600'>
                                Save <BsSave className='w-5 ml-2' />
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default Appraisal