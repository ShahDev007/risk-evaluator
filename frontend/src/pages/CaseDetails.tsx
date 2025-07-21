import React from 'react'
import { useParams } from 'react-router-dom'

const CaseDetails: React.FC = () => {
  const { id } = useParams<{ id: string }>()
  return (
    <div className="container mt-5">
      <h2>Case Details for ID: {id}</h2>
      <p>Risk score: 712</p>
      <p>Summary: Low risk applicant with verified income and identity.</p>
    </div>
  )
}
export default CaseDetails