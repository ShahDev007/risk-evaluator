import React from 'react'
import { Link } from 'react-router-dom'

interface Case {
  id: number;
  name: string;
  score: number;
}

const Dashboard: React.FC = () => {
  const cases: Case[] = [
    { id: 1, name: 'John Doe', score: 712 },
    { id: 2, name: 'Jane Smith', score: 645 }
  ]

  return (
    <div className="container mt-5">
      <h2>Loan Cases</h2>
      <table className="table">
        <thead>
          <tr>
            <th>ID</th><th>Name</th><th>Score</th><th>Action</th>
          </tr>
        </thead>
        <tbody>
          {cases.map(c => (
            <tr key={c.id}>
              <td>{c.id}</td>
              <td>{c.name}</td>
              <td>{c.score}</td>
              <td><Link className="btn btn-secondary btn-sm" to={`/case/${c.id}`}>View</Link></td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}
export default Dashboard