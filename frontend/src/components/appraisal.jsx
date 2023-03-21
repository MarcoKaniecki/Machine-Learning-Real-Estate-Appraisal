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
  
  /* things to be implemented */
  const [utilities, setUtilities] = useState("");
  const [bldgType, setBldgType] = useState("");
  const [houseStyle, setHouseStyle] = useState("");
  const [overallQual, setOverallQual] = useState("");
  const [overallCond, setOverallCond] = useState("");
  const [yearBuilt, setYearBuilt] = useState("");
  const [yearRemod, setYearRemod] = useState("");
  const [exterior1, setExterior1] = useState("");
  const [exterQual, setExterQual] = useState("");
  const [exterCond, setExterCond] = useState("");
  const [foundation, setFoundation] = useState("");
  const [bsmtFinType1, setBsmtFinType1] = useState("");
  const [bsmtFindSF1, setBsmtFindSF1] = useState("");
  const [totalBsmtSF, setTotalBsmtSF] = useState("");
  const [heating, setHeating] = useState("");
  const [heatingQC, setHeatingQC] = useState("");
  const [centralAir, setCentralAir] = useState("");
  const [electrical, setClectrical] = useState("");
  const [fstFloorArea, set1stFloorArea] = useState("");
  const [sndFloorArea, set2ndFloorArea] = useState("");
  const [fullBath, setFullBath] = useState("");
  const [halfBath, setHalfBath] = useState("");
  const [bedroom, setBedroom] = useState("");
  const [kitchen, setKitchen] = useState("");
  const [kitchenQual, setKitchenQual] = useState("");
  const [totRmsAbvGrd, setTotRmsAbvGrd] = useState("");
  const [garageType, setGarageType] = useState("");
  const [garageCars, setGarageCars] = useState("");
  const [garageArea, setGarageArea] = useState("");
  const [garageQual, setGarageQual] = useState("");
  const [woodDeckSF, setWoodDeckSF] = useState("");
  const [fence, setFence] = useState("");
  

  /* combines data in the form and sends it as one package to backend */
  const handleSubmit = async (e) => {
    e.preventDefault();
    let formData = new FormData();
    formData.append("image", image);
    formData.append("zone", zone);
    formData.append("lotArea", lotArea);

    /* things to be implemented */
    formData.append("utilities", utilities);
    formData.append("bldgType", bldgType);
    formData.append("houseStyle", houseStyle);
    formData.append("overallQual", overallQual);
    formData.append("overallCond", overallCond);
    formData.append("yearBuilt", yearBuilt);
    formData.append("yearRemod", yearRemod);
    formData.append("exterior1", exterior1);
    formData.append("exterQual", exterQual);
    formData.append("exterCond", exterCond);
    formData.append("foundation", foundation);
    formData.append("exterCond", exterCond);
    formData.append("bsmtFinType1", bsmtFinType1);
    formData.append("bsmtFindSF1", bsmtFindSF1);
    formData.append("totalBsmtSF", totalBsmtSF);
    formData.append("heating", heating);
    formData.append("heatingQC", heatingQC);
    formData.append("centralAir", centralAir);
    formData.append("electrical", electrical);
    formData.append("fstFloorArea", fstFloorArea);
    formData.append("sndFloorArea", sndFloorArea);
    formData.append("fullBath", fullBath);
    formData.append("halfBath", halfBath);
    formData.append("bedroom", bedroom);
    formData.append("kitchen", kitchen);
    formData.append("kitchenQual", kitchenQual);
    formData.append("totRmsAbvGrd", totRmsAbvGrd);
    formData.append("garageType", garageType);
    formData.append("garageCars", garageCars);
    formData.append("garageArea", garageArea);
    formData.append("garageQual", garageQual);
    formData.append("woodDeckSF", woodDeckSF);
    formData.append("fence", fence);
  

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

                  {/* utilities input field */}
                  <div>
                    <label className="block mb-2 text-sm font-medium text-gray-900">Utilities</label>
                    <select id="utilities" type="text" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-indigo-600 focus:border-indigo-600 block w-full p-2.5 h-10" 
                    onChange={(e) => setUtilities(e.target.value)} required>
                      <option value="AllPub">All public Utilities (E, G, W, and S)</option>
                      <option value="NoSewr">Electricity, Gas, and Water (Septic Tank)</option>
                      <option value="NoSeWa">Electricity and Gas only</option>
                      <option value="ELO">Electricity only</option>
                    </select>
                  </div>

                  <div>
                    <label className="block mb-2 text-sm font-medium text-gray-900">Building Type</label>
                    <select id="bldgType" type="text" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-indigo-600 focus:border-indigo-600 block w-full p-2.5 h-10" 
                    onChange={(e) => setBldgType(e.target.value)} required>
                      <option value="1Fam">Single-family Detached</option>
                      <option value="2FmCon">Two-family Conversion; originally bult as one-family dwelling</option>
                      <option value="Duplx">Duplex</option>
                      <option value="TwnhsE">Townhouse End Unit</option>
                      <option value="TwnhsI">Townhouse Inside Unit</option>
                    </select>
                  </div>


                  <div>
                    <label className="block mb-2 text-sm font-medium text-gray-900">House Style</label>
                    <select id="houseStyle" type="text" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-indigo-600 focus:border-indigo-600 block w-full p-2.5 h-10" 
                    onChange={(e) => setHouseStyle(e.target.value)} required>
                      <option value="1Story">One story</option>
                      <option value="1.5Fin">One and one-half story: 2nd level finished</option>
                      <option value="1.5Unf">One and one-half story: 2nd level unfinished</option>
                      <option value="2Story">Two story</option>
                      <option value="2.5Fin">Two and one-half story: 2nd level finished</option>
                      <option value="2.5Unf">Two and one-half story: 2nd level unfinished</option>
                      <option value="SFoyer">Split Foyer</option>
                      <option value="SLvl">Split Level</option>
                    </select>
                  </div>


                  <div>
                    <label className="block mb-2 text-sm font-medium text-gray-900">Overall Quality: Rates the overall material and finish of the house</label>
                    <select id="overallQual" type="text" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-indigo-600 focus:border-indigo-600 block w-full p-2.5 h-10" 
                    onChange={(e) => setOverallQual(e.target.value)} required>
                      <option value="10">Very Excellent</option>
                      <option value="9">Excellent</option>
                      <option value="8">Very Good</option>
                      <option value="7">Good</option>
                      <option value="6">Above Average</option>
                      <option value="5">Average</option>
                      <option value="4">Below Average</option>
                      <option value="3">Fair</option>
                      <option value="2">Poor</option>
                      <option value="1">Very Poor</option>
                    </select>
                  </div>


                  <div>
                    <label className="block mb-2 text-sm font-medium text-gray-900">Overall Condition: Rates the overall condition of the house</label>
                    <select id="overallCond" type="text" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-indigo-600 focus:border-indigo-600 block w-full p-2.5 h-10" 
                    onChange={(e) => setOverallCond(e.target.value)} required>
                      <option value="10">Very Excellent</option>
                      <option value="9">Excellent</option>
                      <option value="8">Very Good</option>
                      <option value="7">Good</option>
                      <option value="6">Above Average</option>
                      <option value="5">Average</option>
                      <option value="4">Below Average</option>
                      <option value="3">Fair</option>
                      <option value="2">Poor</option>
                      <option value="1">Very Poor</option>
                    </select>
                  </div>

                  <div>
                    <label className="block mb-2 text-sm font-medium text-gray-900">Year Built: Original construction date</label>
                    {/* may want to change max build year dynamically based on current year */}
                    <input id="yearBuilt" type="number" step="1" min="1000" max="3000" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-indigo-600 focus:border-indigo-600 block w-full p-2.5" 
                    value={yearBuilt} onChange={(e) => setYearBuilt(e.target.value)} placeholder="2005" required />
                  </div>

                  <div>
                    <label className="block mb-2 text-sm font-medium text-gray-900">Year Remodelled: Remodel date (same as construction date if no remodeling or additions)</label>
                    {/* may want to change max build year dynamically based on current year */}
                    <input id="yearRemod" type="number" step="1" min="1000" max="3000" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-indigo-600 focus:border-indigo-600 block w-full p-2.5" 
                    value={yearRemod} onChange={(e) => setYearRemod(e.target.value)} placeholder="2005" required />
                  </div>

                  <div>
                    <label className="block mb-2 text-sm font-medium text-gray-900">Exterior 1: Exterior covering on house</label>
                    <select id="exterior1" type="text" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-indigo-600 focus:border-indigo-600 block w-full p-2.5 h-10" 
                    onChange={(e) => setExterior1(e.target.value)} required>
                      <option value="AsbShng">Asbestos Shingles</option>
                      <option value="AsphShn">Asphalt Shingles</option>
                      <option value="BrkComm">Brick Common</option>
                      <option value="BrkFace">Brick Face</option>
                      <option value="CBlock">Cinder Block</option>
                      <option value="CemntBd">Cement Board</option>
                      <option value="HdBoard">Hard Board</option>
                      <option value="ImStucc">Imitation Stucco</option>
                      <option value="MetalSd">Metal Siding</option>
                      <option value="Other">Other</option>
                      <option value="Plywood">Plywood</option>
                      <option value="PreCast">PreCast</option>
                      <option value="Stone">Stone</option>
                      <option value="Stucco">Stucco</option>
                      <option value="VinylSd">Vinyl Siding</option>
                      <option value="Wd Sdng">Wood Siding</option>
                      <option value="WdShing">Wood Shingles</option>
                    </select>
                  </div>

                  <div>
                    <label className="block mb-2 text-sm font-medium text-gray-900">Exterior Quality: Evaluates the quality of the material on the exterior</label>
                    <select id="exterQual" type="text" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-indigo-600 focus:border-indigo-600 block w-full p-2.5 h-10" 
                    onChange={(e) => setExterQual(e.target.value)} required>
                      <option value="Ex">Excellent</option>
                      <option value="Gd">Good</option>
                      <option value="TA">Average/Typical</option>
                      <option value="Fa">Fair</option>
                      <option value="Po">Poor</option>
                    </select>
                  </div>
          

                  <div>
                    <label className="block mb-2 text-sm font-medium text-gray-900">Exterior Condition: Evaluates the present condition of the material on the exterior</label>
                    <select id="exterCond" type="text" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-indigo-600 focus:border-indigo-600 block w-full p-2.5 h-10" 
                    onChange={(e) => setExterCond(e.target.value)} required>
                      <option value="Ex">Excellent</option>
                      <option value="Gd">Good</option>
                      <option value="TA">Average/Typical</option>
                      <option value="Fa">Fair</option>
                      <option value="Po">Poor</option>
                    </select>
                  </div>

                  <div>
                    <label className="block mb-2 text-sm font-medium text-gray-900">Foundation: Type of foundation</label>
                    <select id="foundation" type="text" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-indigo-600 focus:border-indigo-600 block w-full p-2.5 h-10" 
                    onChange={(e) => setFoundation(e.target.value)} required>
                      <option value="BrkTil">Brick & Tile</option>
                      <option value="CBlock">Cinder Block</option>
                      <option value="PConc">Poured Contrete</option>
                      <option value="Slab">Slab</option>
                      <option value="Stone">Stone</option>
                      <option value="Wood">Wood</option>
                    </select>
                  </div>

                  
                  <div>
                    <label className="block mb-2 text-sm font-medium text-gray-900">Basement Finish: Rating of basement finished area</label>
                    <select id="bsmtFinType1" type="text" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-indigo-600 focus:border-indigo-600 block w-full p-2.5 h-10" 
                    onChange={(e) => setBsmtFinType1(e.target.value)} required>
                      <option value="GLQ">Good Living Quarters</option>
                      <option value="ALQ">Average Living Quarters</option>
                      <option value="BLQ">Below Average Living Quarters</option>
                      <option value="Rec">Average Rec Room</option>
                      <option value="LwQ">Low Quality</option>
                      <option value="Unf">Unfinshed</option>
                      <option value="NA">No Basement</option>
                    </select>
                  </div>

                  <div>
                    <label className="block mb-2 text-sm font-medium text-gray-900">Area of Finished Basement: square feet</label>
                    <input id="bsmtFindSF1" type="number" step="1" min="0" max="10000" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-indigo-600 focus:border-indigo-600 block w-full p-2.5" 
                    value={bsmtFindSF1} onChange={(e) => setBsmtFindSF1(e.target.value)} placeholder="200" required />
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