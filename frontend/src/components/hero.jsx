import React from 'react'
import {AiFillGithub} from 'react-icons/ai'
import {BsFillStopwatchFill} from 'react-icons/bs'
import {AiFillLock} from 'react-icons/ai'
import {HiDocument} from 'react-icons/hi'
import { Link } from 'react-scroll'

import bgImg from '../assets/house.png'

const Hero = () => {
    return (
        <div name='home' className='w-full h-screen bg-zinc-200 flex flex-col justify-between'>
            <div className='grid md:grid-cols-2 max-w-[1240px] m-auto'>
                <div className='flex flex-col justify-center md:items-start w-full px-2 py-8'>
                    <p className='text-2xl'>Using Machine Learning for</p>
                    <h1 className='py-3 text-5xl md:text-7xl font-bold'>Real Estate Appraisal</h1>
                    <p className='text-2xl'>This is our Senior Year Project.</p>
                    <button className='py-3 px-6 sm:w-[60%] my-4'><Link to="appraisal" smooth={true} offset={-50} duration={500}>Get Started</Link></button>
                </div>
                <div>
                    <img className='w-full' src={bgImg} alt="/" />
                </div>
                <div className='absolute flex flex-col py-8 md:min-w-[760px] bottom-[5%] 
                mx-1 md:left-1/2 transform md:-translate-x-1/2
                bg-zinc-200 border border-slate-300 rounded-xl text-center shadow-xl'>
                    <p>Features</p>
                    <div className='flex justify-between flex-wrap px-4'>
                        <p className='flex px-4 py-2 text-slate-500'><AiFillGithub className='h-5 text-indigo-600 mr-1' /> Open Source</p>
                        <p className='flex px-4 py-2 text-slate-500'><AiFillLock className='h-5 text-indigo-600 mr-1' /> Secure</p>
                        <p className='flex px-4 py-2 text-slate-500'><HiDocument className='h-5 text-indigo-600 mr-1' /> PDF Format</p>
                        <p className='flex px-4 py-2 text-slate-500'><BsFillStopwatchFill className='h-5 text-indigo-600 mr-1' /> Instant</p>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default Hero