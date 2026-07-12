import { useState, useEffect } from "react"
import axios from "axios"
import MetricCard from "./components/MetricCard"

const API_BASE = "http://localhost:8000"

function App() {
  const [selectedProject, setSelectedProject] = useState(null)
  const [results, setResults] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)
  const [retryCount, setRetryCount] = useState(0)

  useEffect(() => {
    if (!selectedProject) return

    const fetchResults = async () => {
      setLoading(true)
      setError(null)
      setResults(null)
      try {
        const response = await axios.get(`${API_BASE}/evaluate/${selectedProject}`)
        setResults(response.data)
      } catch (err) {
        if (err.response?.status === 503) {
          setError("Evaluation temporarily unavailable due to API rate limits. Please wait a moment and retry.")
        } else {
          setError("Failed to fetch evaluation results. Is the backend running?")
        }
      } finally {
        setLoading(false)
      }
    }
    fetchResults()
  }, [selectedProject, retryCount])

  const projects = [
    { id: "matchforge", label: "MatchForge" },
    { id: "scoute", label: "Scoute" }
  ]

  return (
    <div style={{ display: "flex", minHeight: "100vh" }}>

      {/* Sidebar */}
      <div style={{
        width: "220px",
        backgroundColor: "#161b27",
        padding: "24px 16px",
        borderRight: "1px solid #2a2f3e"
      }}>
        <h2 style={{ fontSize: "18px", fontWeight: "700", marginBottom: "32px", color: "#ffffff" }}>
          Lumeval
        </h2>
        <p style={{ fontSize: "11px", color: "#6b7280", marginBottom: "12px", textTransform: "uppercase", letterSpacing: "0.1em" }}>
          Projects
        </p>
        {projects.map(project => (
          <button
            key={project.id}
            onClick={() => {
              setSelectedProject(project.id)
              setRetryCount(0)
            }}
            style={{
              display: "block",
              width: "100%",
              padding: "10px 12px",
              marginBottom: "4px",
              textAlign: "left",
              backgroundColor: selectedProject === project.id ? "#2a2f3e" : "transparent",
              color: selectedProject === project.id ? "#ffffff" : "#9e9e9e",
              border: "none",
              borderRadius: "6px",
              cursor: "pointer",
              fontSize: "14px",
              fontWeight: selectedProject === project.id ? "600" : "400"
            }}
          >
            {project.label}
          </button>
        ))}
      </div>

      {/* Main content */}
      <div style={{ flex: 1, padding: "40px" }}>

        {/* Welcome screen when no project selected */}
        {!selectedProject && (
          <div style={{
            display: "flex",
            flexDirection: "column",
            alignItems: "center",
            justifyContent: "center",
            height: "80vh",
            color: "#6b7280"
          }}>
            <h1 style={{ fontSize: "32px", fontWeight: "700", color: "#ffffff", marginBottom: "12px" }}>
              Lumeval
            </h1>
            <p style={{ fontSize: "16px" }}>Select a project from the sidebar to run evaluations.</p>
          </div>
        )}

        {/* Project evaluation view */}
        {selectedProject && (
          <>
            <h1 style={{ fontSize: "24px", fontWeight: "700", marginBottom: "8px" }}>
              {projects.find(p => p.id === selectedProject)?.label} Evaluation
            </h1>
            <p style={{ color: "#6b7280", marginBottom: "32px", fontSize: "14px" }}>
              DeepEval metrics run against real inputs and outputs
            </p>

            {loading && <p style={{ color: "#9e9e9e" }}>Running evaluations...</p>}

            {error && (
              <div style={{
                backgroundColor: "#1e2130",
                borderRadius: "8px",
                padding: "20px",
                borderLeft: "4px solid #f44336"
              }}>
                <p style={{ color: "#f44336", fontWeight: "600" }}>Evaluation Unavailable</p>
                <p style={{ color: "#9e9e9e", fontSize: "13px", marginTop: "8px" }}>{error}</p>
                <button
                  onClick={() => setRetryCount(prev => prev + 1)}
                  style={{
                    marginTop: "12px",
                    padding: "8px 16px",
                    backgroundColor: "#2a2f3e",
                    color: "#ffffff",
                    border: "none",
                    borderRadius: "6px",
                    cursor: "pointer",
                    fontSize: "13px"
                  }}
                >
                  Retry
                </button>
              </div>
            )}

            {results && results.evaluations.map((result, index) => (
              <MetricCard
                key={index}
                metric={result.metric}
                score={result.score}
                passed={result.passed}
                reason={result.reason}
              />
            ))}
          </>
        )}
      </div>

    </div>
  )
}

export default App