function MetricCard({ metric, score, passed, reason }) {
    return (
        <div style={{
            backgroundColor: '#1e2130',
            borderRadius: '8px',
            padding: '20px',
            marginBottom: '16px',
            borderLeft: `4px solid ${passed ? '#4caf50' : '#f44336'}`
        }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                <h3 style={{ fontSize: '16px', fontWeight: '600' }}>{metric}</h3>
                <span style={{
                    backgroundColor: passed ? '#1b5e20' : '#b71c1c',
                    color: passed ? '#4caf50' : '#f44336',
                    padding: '4px 12px',
                    borderRadius: '20px',
                    fontSize: '13px',
                    fontWeight: '600'
                }}>
                    {passed ? 'PASSED' : 'FAILED'}
                </span>
            </div>
            <p style={{ fontSize: '28px', fontWeight: '700', margin: '12px 0', color: passed ? '#4caf50' : '#f44336' }}>
                {score.toFixed(2)}
            </p>
            <p style={{ fontSize: '13px', color: '#9e9e9e', lineHeight: '1.5' }}>{reason}</p>
        </div>
    )
}

export default MetricCard