import { useState } from 'react'
import './App.css'

function App() {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleNameChange = (event: any) => {
    setName(event.target.value);
  }
  const handleEmailChange = (event: any) => {
    setEmail(event.target.value);
  }
  const handlePassworChange = (event: any) => {
    setPassword(event.target.value);
  }

  const registerName = (
    <>
      <label htmlFor="name" className='text-black'>Name:</label>
      <input type="text" id="name" name="name" className='bg-gray-200 text-black' value={name} onChange={handleNameChange}/>
    </>
  )

  const handleSubmit = (event: any) => {
    event.preventDefault(); // Prevents the default form submission behavior
    console.log('Name:', name);
    console.log('Email:', email);
    console.log('Password:', password);
  }
  
  const registerSubmit = (
    <>
      <button className='bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 drop-shadow' onClick={handleSubmit}>Submit</button>
    </>
  )
  
  return (
    <>
      <div className='flex gap-2 p-20 max-w-sw bg-white rounded-xl flex-col'>
        <h1 className="text-2xl text-black font-bold text-center">
          Register Here
        </h1>

        {registerName}

        <label htmlFor="email" className='text-black'>Email:</label>
        <input type="email" id="email" name="email" className='bg-gray-200 text-black' value={email} onChange={handleEmailChange}/>

        <label htmlFor="password" className='text-black'>Password:</label>
        <input name="email" className='bg-gray-200 text-black' value={password} onChange={handlePassworChange}/>

        {registerSubmit}

      </div>
    </>
  )
}

export default App
