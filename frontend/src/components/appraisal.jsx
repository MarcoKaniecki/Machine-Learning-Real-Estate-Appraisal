import axios from "axios";
import { useState, useEffect } from "react";
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
      className={`fixed bottom-0 right-0 p-4 m-4 rounded-md bg-gray-700 text-white transition-opacity duration-500 ${show ? "opacity-100" : "opacity-0"
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
  const [property, setProperty] = useState({
    // image: null,
    area: "",
    zone: "",
    lotArea: "",
    utilities: "",
    neighborhood: "",
    bldgType: "",
    houseStyle: "",
    overallQual: "",
    overallCond: "",
    yearBuilt: "",
    yearRemod: "",
    exterior1: "",
    exterQual: "",
    exterCond: "",
    foundation: "",
    bsmtFinType1: "",
    bsmtFindSF1: "",
    totalBsmtSF: "",
    heating: "",
    heatingQC: "",
    centralAir: "",
    electrical: "",
    fullBath: "",
    halfBath: "",
    bedroom: "",
    kitchen: "",
    kitchenQual: "",
    totRmsAbvGrd: "",
    garageType: "",
    garageCars: "",
    garageArea: "",
    garageQual: "",
    woodDeckSF: "",
    fence: "",
  });




  /* combines data in the form and sends it as one package to backend */
  const handleSubmit = async (e) => {
    e.preventDefault();

    // object containing all the properties and their values
    let propertyData = {
      image: image,
      area: property.area,
      zone: property.zone,
      lotArea: property.lotArea,
      utilities: property.utilities,
      neighborhood: property.neighborhood,
      bldgType: property.bldgType,
      houseStyle: property.houseStyle,
      overallQual: property.overallQual,
      overallCond: property.overallCond,
      yearBuilt: property.yearBuilt,
      yearRemod: property.yearRemod,
      exterior1: property.exterior1,
      exterQual: property.exterQual,
      exterCond: property.exterCond,
      foundation: property.foundation,
      bsmtFinType1: property.bsmtFinType1,
      bsmtFindSF1: property.bsmtFindSF1,
      totalBsmtSF: property.totalBsmtSF,
      heating: property.heating,
      heatingQC: property.heatingQC,
      centralAir: property.centralAir,
      electrical: property.electrical,
      fullBath: property.fullBath,
      halfBath: property.halfBath,
      bedroom: property.bedroom,
      kitchen: property.kitchen,
      kitchenQual: property.kitchenQual,
      totRmsAbvGrd: property.totRmsAbvGrd,
      garageType: property.garageType,
      garageCars: property.garageCars,
      garageArea: property.garageArea,
      garageQual: property.garageQual,
      woodDeckSF: property.woodDeckSF,
      fence: property.fence
    };

    let formData = new FormData();
    for (let key in propertyData) {
      formData.append(key, propertyData[key]);
    }


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
                <BsImages className='w-16 h-16 p-4 bg-indigo-600 text-white rounded-lg mt-[-4rem]' />
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
                <BsCardText className='w-16 h-16 p-4 bg-indigo-600 text-white rounded-lg mt-[-4rem]' />
                <h3 className='font-bold text-2xl my-6'>Text</h3>

                <div className="grid gap-6 mb-6 md:grid-cols-2">

                  {/* Area input field */}
                  <div>
                    <label for="area" className="block mb-2 text-sm font-medium text-gray-900">Area</label>
                    <input id="area" type="number" step="1" min="0" max="1000000" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-indigo-600 focus:border-indigo-600 block w-full p-2.5"
                      value={property.area} onChange={(e) => setProperty({ ...property, area: e.target.value })} placeholder="2500" required />
                  </div>

                  {/* Zone/Neighbourhood input field */}
                  <div>
                    <label for="zone" className="block mb-2 text-sm font-medium text-gray-900">Zone</label>
                    <select id="zone" type="text" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-indigo-600 focus:border-indigo-600 block w-full p-2.5 h-10"
                      value={property.zone}
                      onChange={(e) => setProperty({ ...property, zone: e.target.value })} required>
                      <option value="" disabled selected>Select an option</option>
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
                      value={property.lotArea} onChange={(e) => setProperty({ ...property, lotArea: e.target.value })} placeholder="1200" required />
                  </div>

                  {/* utilities input field */}
                  <div>
                    <label className="block mb-2 text-sm font-medium text-gray-900">Utilities</label>
                    <select id="utilities" type="text" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-indigo-600 focus:border-indigo-600 block w-full p-2.5 h-10"
                      onChange={(e) => setProperty({ ...property, utilities: e.target.value })} required>
                      <option value="" disabled selected>Select an option</option>
                      <option value="AllPub">All public Utilities (E, G, W, and S)</option>
                      <option value="NoSewr">Electricity, Gas, and Water (Septic Tank)</option>
                      <option value="NoSeWa">Electricity and Gas only</option>
                      <option value="ELO">Electricity only</option>
                    </select>
                  </div>

                  {/* neighborhood input field */}
                  <div>
                    <label className="block mb-2 text-sm font-medium text-gray-900">Neighborhood</label>
                    <select id="neighborhood" type="text" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-indigo-600 focus:border-indigo-600 block w-full p-2.5 h-10"
                      onChange={(e) => setProperty({ ...property, neighborhood: e.target.value })} required>
                      <option value="" disabled selected>Select an option</option>
                      <option value="Blmngtn">Bloomington Heights</option>
                      <option value="Blueste">Bluestem</option>
                      <option value="BrDale">Briardale</option>
                      <option value="BrkSide">Brookside</option>
                      <option value="ClearCr">Clear Creek</option>
                      <option value="CollgCr">College Creek</option>
                      <option value="Crawfor">Crawford</option>
                      <option value="Edwards">Edwards</option>
                      <option value="Gilbert">Gilbert</option>
                      <option value="IDOTRR">Iowa DOT and Rail Road</option>
                      <option value="MeadowV">Meadow Village</option>
                      <option value="Mitchel">Mitchell</option>
                      <option value="Names">North Ames</option>
                      <option value="NoRidge">Northridge</option>
                      <option value="NPkVill">Northpark Villa</option>
                      <option value="NridgHt">Northridge Heights</option>
                      <option value="NWAmes">Northwest Ames</option>
                      <option value="OldTown">Old Town</option>
                      <option value="SWISU">South & West of Iowa State University</option>
                      <option value="Sawyer">Sawyer</option>
                      <option value="SawyerW">Sawyer West</option>
                      <option value="Somerst">Somerset</option>
                      <option value="StoneBr">Stone Brook</option>
                      <option value="Timber">Timberland</option>
                      <option value="Veenker">Veenker</option>
                    </select>
                  </div>

                  {/* building type input field */}
                  <div>
                    <label className="block mb-2 text-sm font-medium text-gray-900">Building Type</label>
                    <select id="bldgType" type="text" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-indigo-600 focus:border-indigo-600 block w-full p-2.5 h-10"
                      onChange={(e) => setProperty({ ...property, bldgType: e.target.value })} required>
                      <option value="" disabled selected>Select an option</option>
                      <option value="1Fam">Single-family Detached</option>
                      <option value="2FmCon">Two-family Conversion; originally bult as one-family dwelling</option>
                      <option value="Duplx">Duplex</option>
                      <option value="TwnhsE">Townhouse End Unit</option>
                      <option value="TwnhsI">Townhouse Inside Unit</option>
                    </select>
                  </div>

                  {/* house style input field */}
                  <div>
                    <label className="block mb-2 text-sm font-medium text-gray-900">House Style</label>
                    <select id="houseStyle" type="text" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-indigo-600 focus:border-indigo-600 block w-full p-2.5 h-10"
                      onChange={(e) => setProperty({ ...property, houseStyle: e.target.value })} required>
                      <option value="" disabled selected>Select an option</option>
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

                  {/* overall quality input field */}
                  <div>
                    <label className="block mb-2 text-sm font-medium text-gray-900">Overall Quality: Rates the overall material and finish of the house</label>
                    <select id="overallQual" type="text" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-indigo-600 focus:border-indigo-600 block w-full p-2.5 h-10"
                      onChange={(e) => setProperty({ ...property, overallQual: e.target.value })} required>
                      <option value="" disabled selected>Select an option</option>
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

                  {/* overall condtion input field */}
                  <div>
                    <label className="block mb-2 text-sm font-medium text-gray-900">Overall Condition: Rates the overall condition of the house</label>
                    <select id="overallCond" type="text" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-indigo-600 focus:border-indigo-600 block w-full p-2.5 h-10"
                      onChange={(e) => setProperty({ ...property, overallCond: e.target.value })} required>
                      <option value="" disabled selected>Select an option</option>
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

                  {/* build year input field */}
                  <div>
                    <label className="block mb-2 text-sm font-medium text-gray-900">Year Built: Original construction date</label>
                    {/* may want to change max build year dynamically based on current year */}
                    <input id="yearBuilt" type="number" step="1" min="0" max="1000000" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-indigo-600 focus:border-indigo-600 block w-full p-2.5"
                      value={property.yearBuilt} onChange={(e) => setProperty({ ...property, yearBuilt: e.target.value })} placeholder="2005" required />
                  </div>

                  {/* year remodelled input field */}
                  <div>
                    <label className="block mb-2 text-sm font-medium text-gray-900">Year Remodelled: Remodel date (same as construction date if no remodeling or additions)</label>
                    {/* may want to change max build year dynamically based on current year */}
                    <input id="yearRemod" type="number" step="1" min="0" max="1000000" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-indigo-600 focus:border-indigo-600 block w-full p-2.5"
                      value={property.yearRemod} onChange={(e) => setProperty({ ...property, yearRemod: e.target.value })} placeholder="2005" required />
                  </div>

                  {/* main exterior material input field */}
                  <div>
                    <label className="block mb-2 text-sm font-medium text-gray-900">Exterior 1: Exterior covering on house</label>
                    <select id="exterior1" type="text" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-indigo-600 focus:border-indigo-600 block w-full p-2.5 h-10"
                      onChange={(e) => setProperty({ ...property, exterior1: e.target.value })} required>
                      <option value="" disabled selected>Select an option</option>
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

                  {/* exterior quality input field */}
                  <div>
                    <label className="block mb-2 text-sm font-medium text-gray-900">Exterior Quality: Evaluates the quality of the material on the exterior</label>
                    <select id="exterQual" type="text" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-indigo-600 focus:border-indigo-600 block w-full p-2.5 h-10"
                      onChange={(e) => setProperty({ ...property, exterQual: e.target.value })} required>
                      <option value="" disabled selected>Select an option</option>
                      <option value="Ex">Excellent</option>
                      <option value="Gd">Good</option>
                      <option value="TA">Average/Typical</option>
                      <option value="Fa">Fair</option>
                      <option value="Po">Poor</option>
                    </select>
                  </div>

                  {/* exterior condition input field */}
                  <div>
                    <label className="block mb-2 text-sm font-medium text-gray-900">Exterior Condition: Evaluates the present condition of the material on the exterior</label>
                    <select id="exterCond" type="text" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-indigo-600 focus:border-indigo-600 block w-full p-2.5 h-10"
                      onChange={(e) => setProperty({ ...property, exterCond: e.target.value })} required>
                      <option value="" disabled selected>Select an option</option>
                      <option value="Ex">Excellent</option>
                      <option value="Gd">Good</option>
                      <option value="TA">Average/Typical</option>
                      <option value="Fa">Fair</option>
                      <option value="Po">Poor</option>
                    </select>
                  </div>

                  {/* foundation input field */}
                  <div>
                    <label className="block mb-2 text-sm font-medium text-gray-900">Foundation: Type of foundation</label>
                    <select id="foundation" type="text" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-indigo-600 focus:border-indigo-600 block w-full p-2.5 h-10"
                      onChange={(e) => setProperty({ ...property, foundation: e.target.value })} required>
                      <option value="" disabled selected>Select an option</option>
                      <option value="BrkTil">Brick & Tile</option>
                      <option value="CBlock">Cinder Block</option>
                      <option value="PConc">Poured Contrete</option>
                      <option value="Slab">Slab</option>
                      <option value="Stone">Stone</option>
                      <option value="Wood">Wood</option>
                    </select>
                  </div>

                  {/* basement finish type input field */}
                  <div>
                    <label className="block mb-2 text-sm font-medium text-gray-900">Basement Finish: Rating of basement finished area</label>
                    <select id="bsmtFinType1" type="text" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-indigo-600 focus:border-indigo-600 block w-full p-2.5 h-10"
                      onChange={(e) => setProperty({ ...property, bsmtFinType1: e.target.value })} required>
                      <option value="" disabled selected>Select an option</option>
                      <option value="GLQ">Good Living Quarters</option>
                      <option value="ALQ">Average Living Quarters</option>
                      <option value="BLQ">Below Average Living Quarters</option>
                      <option value="Rec">Average Rec Room</option>
                      <option value="LwQ">Low Quality</option>
                      <option value="Unf">Unfinshed</option>
                      <option value="NA">No Basement</option>
                    </select>
                  </div>

                  {/* size of finished basement input field */}
                  <div>
                    <label className="block mb-2 text-sm font-medium text-gray-900">Area of Finished Basement in square feet</label>
                    <input id="bsmtFindSF1" type="number" step="1" min="0" max="1000000" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-indigo-600 focus:border-indigo-600 block w-full p-2.5"
                      value={property.bsmtFindSF1} onChange={(e) => setProperty({ ...property, bsmtFindSF1: e.target.value })} placeholder="500" required />
                  </div>

                  {/* total size of basement input field */}
                  <div>
                    <label className="block mb-2 text-sm font-medium text-gray-900">Total Area of Basement in square feet</label>
                    <input id="totalBsmtSF" type="number" step="1" min="0" max="1000000" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-indigo-600 focus:border-indigo-600 block w-full p-2.5"
                      value={property.totalBsmtSF} onChange={(e) => setProperty({ ...property, totalBsmtSF: e.target.value })} placeholder="500" required />
                  </div>

                  {/* heating type input field */}
                  <div>
                    <label className="block mb-2 text-sm font-medium text-gray-900">Heating: Type of heating</label>
                    <select id="heating" type="text" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-indigo-600 focus:border-indigo-600 block w-full p-2.5 h-10"
                      onChange={(e) => setProperty({ ...property, heating: e.target.value })} required>
                      <option value="" disabled selected>Select an option</option>
                      <option value="Floor">Floor Furnace</option>
                      <option value="GasA">Gas forced warm air furnace</option>
                      <option value="GasW">Gas hot water or steam heat</option>
                      <option value="Grav">Gravity furnace</option>
                      <option value="OthW">Hot water or steam heat other than gas</option>
                      <option value="Wall">Wall furnace</option>
                    </select>
                  </div>

                  {/* heaitng quality and condition input field */}
                  <div>
                    <label className="block mb-2 text-sm font-medium text-gray-900">Heating quality and condition</label>
                    <select id="heatingQC" type="text" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-indigo-600 focus:border-indigo-600 block w-full p-2.5 h-10"
                      onChange={(e) => setProperty({ ...property, heatingQC: e.target.value })} required>
                      <option value="" disabled selected>Select an option</option>
                      <option value="Ex">Excellent</option>
                      <option value="Gd">Good</option>
                      <option value="TA">Average/Typical</option>
                      <option value="Fa">Fair</option>
                      <option value="Po">Poor</option>
                    </select>
                  </div>

                  {/* central air input field */}
                  <div>
                    <label className="block mb-2 text-sm font-medium text-gray-900">Central air conditioning</label>
                    <select id="centralAir" type="text" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-indigo-600 focus:border-indigo-600 block w-full p-2.5 h-10"
                      onChange={(e) => setProperty({ ...property, centralAir: e.target.value })} required>
                      <option value="" disabled selected>Select an option</option>
                      <option value="N">No</option>
                      <option value="Y">Yes</option>
                    </select>
                  </div>

                  {/* electrical type input field */}
                  <div>
                    <label className="block mb-2 text-sm font-medium text-gray-900">Electrical system</label>
                    <select id="electrical" type="text" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-indigo-600 focus:border-indigo-600 block w-full p-2.5 h-10"
                      onChange={(e) => setProperty({ ...property, electrical: e.target.value })} required>
                      <option value="" disabled selected>Select an option</option>
                      <option value="SBrkr">Standard Circuit Breakers & Romex</option>
                      <option value="FuseA">Fuse Box over 60 AMP and all Romex wiring (Average)</option>
                      <option value="FuseF">60 AMP Fuse Box and mostly Romex wiring (Fair)</option>
                      <option value="FuseP">60 AMP Fuse Box and mostly knob & tube wiring (poor)</option>
                      <option value="Mix">Mixed</option>
                    </select>
                  </div>

                  {/* number of full baths input field */}
                  <div>
                    <label className="block mb-2 text-sm font-medium text-gray-900">Number of full bathrooms</label>
                    <input id="fullBath" type="number" step="1" min="0" max="1000" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-indigo-600 focus:border-indigo-600 block w-full p-2.5"
                      value={property.fullBath} onChange={(e) => setProperty({ ...property, fullBath: e.target.value })} placeholder="2" required />
                  </div>

                  {/* number of half baths input field */}
                  <div>
                    <label className="block mb-2 text-sm font-medium text-gray-900">Number of half bathrooms</label>
                    <input id="halfBath" type="number" step="1" min="0" max="1000" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-indigo-600 focus:border-indigo-600 block w-full p-2.5"
                      value={property.halfBath} onChange={(e) => setProperty({ ...property, halfBath: e.target.value })} placeholder="1" required />
                  </div>

                  {/* number of bedrooms input field */}
                  <div>
                    <label className="block mb-2 text-sm font-medium text-gray-900">Number of Bedrooms (not including basement bedrooms)</label>
                    <input id="bedroom" type="number" step="1" min="0" max="1000" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-indigo-600 focus:border-indigo-600 block w-full p-2.5"
                      value={property.bedroom} onChange={(e) => setProperty({ ...property, bedroom: e.target.value })} placeholder="3" required />
                  </div>

                  {/* number of kitchens input field */}
                  <div>
                    <label className="block mb-2 text-sm font-medium text-gray-900">Number of Kitchens</label>
                    <input id="kitchen" type="number" step="1" min="0" max="1000" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-indigo-600 focus:border-indigo-600 block w-full p-2.5"
                      value={property.kitchen} onChange={(e) => setProperty({ ...property, kitchen: e.target.value })} placeholder="1" required />
                  </div>

                  {/* kitchen quality input field */}
                  <div>
                    <label className="block mb-2 text-sm font-medium text-gray-900">Kitchen quality</label>
                    <select id="kitchenQual" type="text" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-indigo-600 focus:border-indigo-600 block w-full p-2.5 h-10"
                      onChange={(e) => setProperty({ ...property, kitchenQual: e.target.value })} required>
                      <option value="" disabled selected>Select an option</option>
                      <option value="Ex">Excellent</option>
                      <option value="Gd">Good</option>
                      <option value="TA">Average/Typical</option>
                      <option value="Fa">Fair</option>
                      <option value="Po">Poor</option>
                    </select>
                  </div>

                  {/* total rooms above ground input field */}
                  <div>
                    <label className="block mb-2 text-sm font-medium text-gray-900">Total rooms above grade (does not include bathrooms)</label>
                    <input id="totRmsAbvGrd" type="number" step="1" min="0" max="1000" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-indigo-600 focus:border-indigo-600 block w-full p-2.5"
                      value={property.totRmsAbvGrd} onChange={(e) => setProperty({ ...property, totRmsAbvGrd: e.target.value })} placeholder="8" required />
                  </div>

                  {/* garage type input field */}
                  <div>
                    <label className="block mb-2 text-sm font-medium text-gray-900">Garage location</label>
                    <select id="garageType" type="text" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-indigo-600 focus:border-indigo-600 block w-full p-2.5 h-10"
                      onChange={(e) => setProperty({ ...property, garageType: e.target.value })} required>
                      <option value="" disabled selected>Select an option</option>
                      <option value="2Types">More than one type of garage</option>
                      <option value="Attchd">Attached to home</option>
                      <option value="Basment">Basement Garage</option>
                      <option value="BuiltIn">Built-In (Garage part of house - typically has room above garage)</option>
                      <option value="CarPort">Car Port</option>
                      <option value="Detchd">Detached from home</option>
                      <option value="NA">No Garage</option>
                    </select>
                  </div>

                  {/* number of cars garage can fit input field */}
                  <div>
                    <label className="block mb-2 text-sm font-medium text-gray-900">Size of garage in car capacity</label>
                    <input id="garageCars" type="number" step="1" min="0" max="1000" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-indigo-600 focus:border-indigo-600 block w-full p-2.5"
                      value={property.garageCars} onChange={(e) => setProperty({ ...property, garageCars: e.target.value })} placeholder="2" required />
                  </div>

                  {/* garage area input field */}
                  <div>
                    <label className="block mb-2 text-sm font-medium text-gray-900">Size of garage in square feet</label>
                    <input id="garageArea" type="number" step="1" min="0" max="1000000" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-indigo-600 focus:border-indigo-600 block w-full p-2.5"
                      value={property.garageArea} onChange={(e) => setProperty({ ...property, garageArea: e.target.value })} placeholder="400" required />
                  </div>

                  {/* garage quality input field */}
                  <div>
                    <label className="block mb-2 text-sm font-medium text-gray-900">Garage quality</label>
                    <select id="garageQual" type="text" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-indigo-600 focus:border-indigo-600 block w-full p-2.5 h-10"
                      onChange={(e) => setProperty({ ...property, garageQual: e.target.value })} required>
                      <option value="" disabled selected>Select an option</option>
                      <option value="Ex">Excellent</option>
                      <option value="Gd">Good</option>
                      <option value="TA">Average/Typical</option>
                      <option value="Fa">Fair</option>
                      <option value="Po">Poor</option>
                      <option value="NA">No Garage</option>
                    </select>
                  </div>

                  {/* size of wooden deck input field */}
                  <div>
                    <label className="block mb-2 text-sm font-medium text-gray-900">Wood deck area in square feet</label>
                    <input id="woodDeckSF" type="number" step="1" min="0" max="100000" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-indigo-600 focus:border-indigo-600 block w-full p-2.5"
                      value={property.woodDeckSF} onChange={(e) => setProperty({ ...property, woodDeckSF: e.target.value })} placeholder="200" required />
                  </div>

                  {/* fence input field */}
                  <div>
                    <label className="block mb-2 text-sm font-medium text-gray-900">Fence quality</label>
                    <select id="fence" type="text" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-indigo-600 focus:border-indigo-600 block w-full p-2.5 h-10"
                      onChange={(e) => setProperty({ ...property, fence: e.target.value })} required>
                      <option value="" disabled selected>Select an option</option>
                      <option value="GdPrv">Good Privacy</option>
                      <option value="MnPrv">Minimum Privacy</option>
                      <option value="GdWo">Good Wood</option>
                      <option value="MnWw">Minimum Wood/Wire</option>
                      <option value="NA">No Fence</option>
                    </select>
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