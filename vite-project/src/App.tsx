import './App.css'


function App() {
  return (
    <>
      <div className='flex gap-2 p-20 max-w-sw bg-white rounded-xl flex-col'>
        <h1 className="text-2xl text-black font-bold text-center">
          Login
        </h1>
        <label htmlFor="name" className='text-black'>Name:</label>
        <input type="text" id="name" name="name" className='bg-gray-200 text-black'/>

        <label htmlFor="email" className='text-black'>Email:</label>
        <input type="email" id="email" name="email" className='bg-gray-200 text-black'/>

        <label htmlFor="password" className='text-black'>Password:</label>
        <input type="email" id="email" name="email" className='bg-gray-200 text-black'/>

        <button className='bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4'>Submit</button>
      </div>
    </>
  )
}

export default App
