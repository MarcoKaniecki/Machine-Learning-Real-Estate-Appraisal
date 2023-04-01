import React from 'react';
import { BsFillPatchCheckFill } from 'react-icons/bs';

const Methodology = () => {
    return (
        <div name='methodology' className='w-full my-32'>
            <div className='max-w-[1240px] mx-auto px-2'>
                <h2 className='text-5xl font-bold text-center'>Methodology</h2>
                <p className='text-2xl py-8 text-gray-500 text-center'>Lorem ipsum dolor sit amet consectetur adipisicing elit. Perspiciatis omnis eaque eos sunt sit ea consequuntur totam animi recusandae delectus.</p>

                <div className='grid sm:grid-cols-3 lg:grid-cols-3 gap-4 pt-4'>
                    <div className='flex'>
                        <div>
                            <BsFillPatchCheckFill className='text-indigo-600 w-7 h-7 mr-4'/>  
                        </div>
                        
                        <div>
                            <h3 className='font-bold text-lg'>Django Python</h3>
                            <p className='text-lg pt-2 pb-4'>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Quam quis labore debitis nemo velit impedit!</p>
                        </div>
                    </div>

                    <div className='flex'>
                        <div>
                            <BsFillPatchCheckFill className='text-indigo-600 w-7 h-7 mr-4'/>  
                        </div>
                        
                        <div>
                            <h3 className='font-bold text-lg'>Random Forest Regression</h3>
                            <p className='text-lg pt-2 pb-4'>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Quam quis labore debitis nemo velit impedit!</p>
                        </div>
                    </div>

                    <div className='flex'>
                        <div>
                            <BsFillPatchCheckFill className='text-indigo-600 w-7 h-7 mr-4'/>  
                        </div>
                        
                        <div>
                            <h3 className='font-bold text-lg'>SQLite</h3>
                            <p className='text-lg pt-2 pb-4'>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Quam quis labore debitis nemo velit impedit!</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default Methodology