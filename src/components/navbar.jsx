import React, {useState} from 'react'
import {FaBars} from 'react-icons/fa'
import {ImCross} from 'react-icons/im'

const Navbar = () => {
        const [nav, setNav] = useState(false)
        const handleClick = () => setNav(!nav)

    return (
        <div className='w-screen h-[80px] z-10 bg-zinc-200 fixed drop-shadow-lg'>
            <div className='px-2 flex justify-between items-center w-full h-full'>
                <div className='flex items-center'>
                    <h1 className='text-3xl font-bold mr-4 sm:text-4xl'>READL.</h1>
                    <ul className='hidden md:flex'>
                        <li>Home</li>
                        <li>About</li>
                        <li>Appraisal</li>
                        <li>Documentation</li>
                    </ul>
                </div>
                <div className='hidden md:flex pr-4'>
                    <button className='border-none bg-transparent text-black mr-4'>
                        Some
                    </button>
                    <button className='px-8 py-3'>Thing?</button>
                </div>

                {/* Anything over minimum width the button will be hidden */}
                <div className='md:hidden' onClick={handleClick}>
                    {!nav ? <FaBars className='w-5' /> : <ImCross className='w-5' />}
                </div>
            </div>

            {/* Drop-dowm menu for mobile sized screens */}
            <ul className={!nav ? 'hidden' : 'absolute bg-zinc-200 w-full px-8'}>
                <li className='border-b-2 border-zinc-300 w-full'>Home</li>
                <li className='border-b-2 border-zinc-300 w-full'>About</li>
                <li className='border-b-2 border-zinc-300 w-full'>Appraisal</li>
                <li className='border-b-2 border-zinc-300 w-full'>Documentation</li>
                
                {/* Stack buttons ontop of one another using flex and flex-col */}
                <div className='flex flex-col my-4'>
                    <button className='bg-transparent text-indigo-600 px-8 py-3 mb-4'>Some</button>
                    <button className='px-8 py-3'>Thing?</button>
                </div>
            </ul>
        </div>
        
    )
}

export default Navbar