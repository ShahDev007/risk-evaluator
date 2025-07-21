import React from 'react'
import { Link } from 'react-router-dom'
const App: React.FC = () => {
  return (
    <div className="container mt-5 text-center">
      <h1>Welcome to RiskIQ Case Manager</h1>
      <Link className="btn btn-primary mt-3" to="/login">Go to Login</Link>
    </div>
  )
}
export default App