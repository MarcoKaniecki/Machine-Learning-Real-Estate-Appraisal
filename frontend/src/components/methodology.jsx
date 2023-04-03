import React from 'react';
import { BsFillPatchCheckFill } from 'react-icons/bs';

const Methodology = () => {
    return (
        <div name='methodology' className='w-full mt-32 mb-8'>
            <div className='max-w-[1240px] mx-auto px-2'>
                <h2 className='text-5xl font-bold text-center'>Methodology</h2>
                <p className='text-2xl py-8 text-gray-500 text-center'>Our project was initiated as a Senior Year Capstone Project at Dalhousie University. 
                Here are some of the key components utilized to form the project's functionality:</p>

                <div className='grid sm:grid-cols-3 lg:grid-cols-3 gap-4 pt-4'>
                    <div className='flex'>
                        <div>
                            <BsFillPatchCheckFill className='text-indigo-600 w-7 h-7 mr-4'/>  
                        </div>
                        
                        <div>
                            <h3 className='font-bold text-lg'>Django Python</h3>
                            <p className='text-lg pt-2 pb-4'>Django Python connects our frontend web page with the services at the backend.</p>
                        </div>
                    </div>

                    <div className='flex'>
                        <div>
                            <BsFillPatchCheckFill className='text-indigo-600 w-7 h-7 mr-4'/>  
                        </div>
                        
                        <div>
                            <h3 className='font-bold text-lg'>Random Forest Regression</h3>
                            <p className='text-lg pt-2 pb-4'>Appraisals are completed using a Random Forest Regression Model, allowing over 90% accuracy in price prediction.</p>
                        </div>
                    </div>

                    <div className='flex'>
                        <div>
                            <BsFillPatchCheckFill className='text-indigo-600 w-7 h-7 mr-4'/>  
                        </div>
                        
                        <div>
                            <h3 className='font-bold text-lg'>SQLite3</h3>
                            <p className='text-lg pt-2 pb-4'>The dataset is stored in a SQLite3 database, where comparable homes will be extracted from automatically during the appraisal.</p>
                        </div>
                    </div>
                </div>
                <p className='text-xl py-8 text-gray-500 text-center'>To discuss collaboration opportunities, or to request availability in your region please 
                    <a href="mailto:erin.chiasson@dal.ca; mr290856@dal.ca"> contact us</a>.
                </p>
            </div>
        </div>
    )
}

export default Methodology