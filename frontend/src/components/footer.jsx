import React from 'react'

import {FaGithub} from 'react-icons/fa'

const Footer = () => {
    return (
        <div className='w-full mt-24 bg-slate-900 text-gray-300 py-y px-2'>
            <div className='max-w-[1240px] mx-auto grid grid-cols-2 md:grid-cols-6 border-b-2 border-gray-600 py-8'>
                <div>
                    <h6 className='font-bold uppercase pt-2'>Support</h6>
                    <ul>
                        <a href="https://github.com/MarcoKaniecki/Machine-Learning-Real-Estate-Appraisal">
                            <li className='py-1'>GitHub</li>
                        </a>
                        <a href="mailto:erin.chiasson@dal.ca; mr290856@dal.ca">
                            <li className='py-1'>Contact</li>
                        </a>
                    </ul>
                </div>
            </div>

            <div className='flex flex-col max-w-[1240px] px-2 py-4 mx-auto justify-between sm:flex-row text-center text-gray-500'>
                <p className='py-4'>2022 REALM Group</p>
                {/*TODO the github icon needs to get moved to the right a bit*/}
                <div className='flex justify-between sm:w-[300px] pt-4 text-2xl'>
                    <FaGithub href="https://github.com/MarcoKaniecki/Machine-Learning-Real-Estate-Appraisal"/>
                </div>
            </div>
        </div>
    )
}

export default Footer