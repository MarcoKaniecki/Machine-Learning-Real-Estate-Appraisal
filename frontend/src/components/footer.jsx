import React from 'react'

import {FaGithub} from 'react-icons/fa'

const Footer = () => {
    return (
        <div className='w-full mt-8 bg-slate-900 text-gray-300 py-y px-2'>
            <div className='max-w-[1240px] mx-auto grid grid-cols-2 md:grid-cols-6 border-b-2 border-gray-600 py-8'>
                <div>
                    <h6 className='font-bold uppercase pt-2'>Support</h6>
                    <ul>
                        <a href="https://github.com/MarcoKaniecki/Machine-Learning-Real-Estate-Appraisal">
                            <li className='py-1 hover:text-indigo-600'>GitHub</li>
                        </a>
                        <a href="mailto:erin.chiasson@dal.ca; mr290856@dal.ca">
                            <li className='py-1 hover:text-indigo-600'>Contact</li>
                        </a>
                    </ul>
                </div>
            </div>

            <div className='flex flex-col max-w-[1240px] px-2 py-4 mx-auto justify-between sm:flex-row text-center text-gray-500'>
                <p className='py-4'>2022 REALM Group</p>
                <div className='flex justify-end sm:w-[300px] pt-4 text-2xl hover:text-indigo-600'>
                    <a href="https://github.com/MarcoKaniecki/Machine-Learning-Real-Estate-Appraisal">
                        <FaGithub />
                    </a>
                </div>
            </div>
        </div>
    )
}

export default Footer