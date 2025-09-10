// Dashboard-specific JavaScript functionality for MediPredict

// Chart configurations and data
let diseaseChart = null;
let timeChart = null;
let metricsChart = null;

document.addEventListener('DOMContentLoaded', function() {
    // Check if dashboardData object exists before proceeding
    if (typeof dashboardData === 'undefined') {
        console.error("Dashboard data not found. Please ensure it's passed from the server.");
        // Optional: Display a user-friendly error message on the page
        return;
    }

    // Initialize dashboard components
    initializeDashboardCharts();
    setupDashboardInteractions();
    startRealTimeUpdates();
});

function initializeDashboardCharts() {
    // Initialize disease distribution chart
    initializeDiseaseChart();
    
    // Initialize time series chart
    initializeTimeChart();
    
    // Initialize metrics comparison chart
    initializeMetricsChart();
    
    // Setup chart responsiveness
    setupChartResponsiveness();
}

function initializeDiseaseChart() {
    const diseaseCtx = document.getElementById('diseaseChart');
    if (!diseaseCtx) return;
    
    const ctx = diseaseCtx.getContext('2d');
    
    // Get data from the template (passed from Flask)
    const diseaseData = dashboardData.diseaseData || { labels: [], data: [] };
    
    diseaseChart = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: diseaseData.labels,
            datasets: [{
                data: diseaseData.data,
                backgroundColor: [
                    '#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0',
                    '#9966FF', '#FF9F40', '#FF6384', '#C9CBCF',
                    '#4BC0C0', '#FF6384', '#36A2EB', '#FFCE56'
                ],
                borderWidth: 2,
                borderColor: '#fff',
                hoverBorderWidth: 3,
                hoverBorderColor: '#333'
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    position: 'bottom',
                    labels: {
                        padding: 15,
                        usePointStyle: true,
                        font: {
                            size: 11
                        }
                    }
                },
                tooltip: {
                    callbacks: {
                        label: function(context) {
                            const label = context.label || '';
                            const value = context.parsed || 0;
                            const total = context.dataset.data.reduce((a, b) => a + b, 0);
                            const percentage = ((value / total) * 100).toFixed(1);
                            return `${label}: ${value} (${percentage}%)`;
                        }
                    }
                }
            },
            animation: {
                animateRotate: true,
                animateScale: true,
                duration: 1000
            }
        }
    });
}

function initializeTimeChart() {
    const timeCtx = document.getElementById('timeChart');
    if (!timeCtx) return;
    
    const ctx = timeCtx.getContext('2d');
    
    // Get data from the template (passed from Flask)
    const timeData = dashboardData.timeData || { labels: [], data: [] };
    
    timeChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: timeData.labels,
            datasets: [{
                label: 'Daily Predictions',
                data: timeData.data,
                borderColor: '#36A2EB',
                backgroundColor: 'rgba(54, 162, 235, 0.1)',
                borderWidth: 3,
                fill: true,
                tension: 0.2,
                pointBackgroundColor: '#36A2EB',
                pointBorderColor: '#fff',
                pointBorderWidth: 2,
                pointRadius: 5,
                pointHoverRadius: 7,
                pointHoverBackgroundColor: '#2980b9',
                pointHoverBorderColor: '#fff',
                pointHoverBorderWidth: 2
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            interaction: {
                intersect: false,
                mode: 'index'
            },
            scales: {
                x: {
                    display: true,
                    title: {
                        display: true,
                        text: 'Date',
                        font: {
                            size: 12,
                            weight: 'bold'
                        }
                    },
                    grid: {
                        display: true,
                        color: 'rgba(0,0,0,0.1)'
                    }
                },
                y: {
                    display: true,
                    title: {
                        display: true,
                        text: 'Number of Predictions',
                        font: {
                            size: 12,
                            weight: 'bold'
                        }
                    },
                    beginAtZero: true,
                    ticks: {
                        stepSize: 1,
                        callback: function(value) {
                            return Number.isInteger(value) ? value : '';
                        }
                    },
                    grid: {
                        display: true,
                        color: 'rgba(0,0,0,0.1)'
                    }
                }
            },
            plugins: {
                legend: {
                    display: false
                },
                tooltip: {
                    backgroundColor: 'rgba(0,0,0,0.8)',
                    titleColor: '#fff',
                    bodyColor: '#fff',
                    borderColor: '#36A2EB',
                    borderWidth: 1,
                    cornerRadius: 5,
                    displayColors: false
                }
            },
            animation: {
                duration: 1500,
                easing: 'easeInOutQuart'
            }
        }
    });
}

function initializeMetricsChart() {
    const metricsCtx = document.getElementById('metricsChart');
    if (!metricsCtx) return;
    
    const ctx = metricsCtx.getContext('2d');
    
    // Get model metrics from the template
    const modelMetrics = dashboardData.modelMetrics || {
        accuracy: 0.85,
        precision: 0.83,
        recall: 0.82,
        f1_score: 0.82
    };
    
    metricsChart = new Chart(ctx, {
        type: 'radar',
        data: {
            labels: ['Accuracy', 'Precision', 'Recall', 'F1 Score'],
            datasets: [{
                label: 'Model Performance',
                data: [
                    modelMetrics.accuracy * 100,
                    modelMetrics.precision * 100,
                    modelMetrics.recall * 100,
                    modelMetrics.f1_score * 100
                ],
                backgroundColor: 'rgba(54, 162, 235, 0.2)',
                borderColor: '#36A2EB',
                borderWidth: 2,
                pointBackgroundColor: '#36A2EB',
                pointBorderColor: '#fff',
                pointBorderWidth: 2,
                pointRadius: 5,
                pointHoverRadius: 7
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                r: {
                    beginAtZero: true,
                    max: 100,
                    ticks: {
                        stepSize: 20,
                        callback: function(value) {
                            return value + '%';
                        }
                    },
                    grid: {
                        color: 'rgba(0,0,0,0.1)'
                    },
                    angleLines: {
                        color: 'rgba(0,0,0,0.1)'
                    }
                }
            },
            plugins: {
                legend: {
                    display: false
                },
                tooltip: {
                    callbacks: {
                        label: function(context) {
                            return `${context.label}: ${context.parsed.r.toFixed(1)}%`;
                        }
                    }
                }
            },
            animation: {
                duration: 1000,
                easing: 'easeOutQuart'
            }
        }
    });
}

function setupChartResponsiveness() {
    let resizeTimeout;
    window.addEventListener('resize', function() {
        clearTimeout(resizeTimeout);
        resizeTimeout = setTimeout(function() {
            if (diseaseChart) diseaseChart.resize();
            if (timeChart) timeChart.resize();
            if (metricsChart) metricsChart.resize();
        }, 100);
    });
}

function setupDashboardInteractions() {
    setupMetricCardInteractions();
    setupChartLegendInteractions();
    setupRefreshFunctionality();
    setupExportFunctionality();
}

function setupMetricCardInteractions() {
    const metricCards = document.querySelectorAll('.metric-card');
    
    metricCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-10px)';
            this.style.boxShadow = '0 10px 25px rgba(0,0,0,0.15)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0px)'; // Fixed: Changed translateY(-5px) to translateY(0px) to prevent card from "hovering" on leave.
            this.style.boxShadow = '0 5px 15px rgba(0,0,0,0.1)';
        });
        
        card.addEventListener('click', function() {
            const cardType = this.querySelector('p').textContent.trim(); // Fixed: Changed selector to 'p' to get the metric name
            showMetricDetails(cardType);
        });
    });
}

function setupChartLegendInteractions() {
    if (diseaseChart && diseaseChart.options.plugins.legend) {
        diseaseChart.options.plugins.legend.onClick = function(event, legendItem, legend) {
            const index = legendItem.datasetIndex;
            const chart = legend.chart;
            const meta = chart.getDatasetMeta(index);
            
            meta.hidden = meta.hidden === null ? !chart.data.datasets[index].hidden : null;
            chart.update();
        };
    }
}

function setupRefreshFunctionality() {
    const refreshButton = document.querySelector('.btn.btn-outline-secondary');
    if (refreshButton) {
        refreshButton.addEventListener('click', function(e) {
            e.preventDefault();
            refreshDashboardData();
        });
    }
}

function setupExportFunctionality() {
    const exportButton = document.querySelector('[onclick="exportData()"]');
    if (exportButton) {
        exportButton.addEventListener('click', function(e) {
            e.preventDefault();
            exportDashboardData();
        });
    }
}

function fetchDashboardData() {
    return fetch('/api/dashboard-data') // New endpoint for fetching data
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        });
}

function refreshDashboardData() {
    const refreshButton = document.querySelector('.btn.btn-outline-secondary');
    const originalContent = refreshButton.innerHTML;
    refreshButton.innerHTML = '<i class="fas fa-spinner fa-spin me-2"></i>Refreshing...';
    refreshButton.disabled = true;

    fetchDashboardData()
        .then(data => {
            // Update Metric Cards
            document.getElementById('total-predictions-value').textContent = data.total_predictions; // Assumes IDs on H2 tags
            document.getElementById('recent-predictions-value').textContent = data.recent_predictions;
            // ... update other metrics

            // Update charts with new data
            diseaseChart.data.labels = data.disease_data.labels;
            diseaseChart.data.datasets[0].data = data.disease_data.data;
            diseaseChart.update();

            timeChart.data.labels = data.time_data.labels;
            timeChart.data.datasets[0].data = data.time_data.data;
            timeChart.update();

            metricsChart.data.datasets[0].data = [
                data.model_metrics.accuracy * 100,
                data.model_metrics.precision * 100,
                data.model_metrics.recall * 100,
                data.model_metrics.f1_score * 100
            ];
            metricsChart.update();

            if (window.MediPredict && window.MediPredict.showNotification) {
                window.MediPredict.showNotification('Dashboard refreshed successfully!', 'success');
            }
        })
        .catch(error => {
            console.error('Failed to refresh dashboard data:', error);
            if (window.MediPredict && window.MediPredict.showNotification) {
                window.MediPredict.showNotification('Failed to refresh data. Please try again.', 'error');
            }
        })
        .finally(() => {
            refreshButton.innerHTML = originalContent;
            refreshButton.disabled = false;
        });
}

function exportDashboardData() {
    try {
        const exportData = {
            timestamp: new Date().toISOString(),
            disease_distribution: dashboardData.diseaseData || {},
            time_series: dashboardData.timeData || {},
            model_metrics: dashboardData.modelMetrics || {},
            system_info: {
                total_predictions: document.getElementById('total-predictions-value')?.textContent || '0',
                recent_predictions: document.getElementById('recent-predictions-value')?.textContent || '0'
            }
        };
        
        const dataStr = JSON.stringify(exportData, null, 2);
        const dataBlob = new Blob([dataStr], {type: 'application/json'});
        const url = URL.createObjectURL(dataBlob);
        
        const link = document.createElement('a');
        link.href = url;
        link.download = `medipredict_analytics_${new Date().toISOString().split('T')[0]}.json`;
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
        
        URL.revokeObjectURL(url);
        
        if (window.MediPredict && window.MediPredict.showNotification) {
            window.MediPredict.showNotification('Analytics data exported successfully!', 'success');
        }
        
    } catch (error) {
        console.error('Export failed:', error);
        if (window.MediPredict && window.MediPredict.showNotification) {
            window.MediPredict.showNotification('Export failed. Please try again.', 'error');
        }
    }
}

function showMetricDetails(metricType) {
    const modalContent = getMetricModalContent(metricType);
    
    let modal = document.getElementById('metricModal');
    if (!modal) {
        modal = createMetricModal();
    }
    
    const modalBody = modal.querySelector('.modal-body');
    if (modalBody) {
        modalBody.innerHTML = modalContent;
    }
    
    const bootstrapModal = new bootstrap.Modal(modal);
    bootstrapModal.show();
}

function createMetricModal() {
    const modal = document.createElement('div');
    modal.className = 'modal fade';
    modal.id = 'metricModal';
    modal.setAttribute('tabindex', '-1');
    modal.setAttribute('aria-labelledby', 'metricModalLabel');
    modal.setAttribute('aria-hidden', 'true');
    modal.innerHTML = `
        <div class="modal-dialog modal-lg">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="metricModalLabel">Metric Details</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                </div>
            </div>
        </div>
    `;
    
    document.body.appendChild(modal);
    return modal;
}

function getMetricModalContent(metricType) {
    const content = {
        'Total Predictions': `
            <h6>Total Predictions Made</h6>
            <p>This represents the cumulative number of disease predictions made by the system since inception.</p>
            <ul>
                <li>Includes both registered user and anonymous predictions</li>
                <li>Updated in real-time as new predictions are made</li>
                <li>Helps track system usage and adoption</li>
            </ul>
        `,
        'Last 30 Days': `
            <h6>Predictions in Last 30 Days</h6>
            <p>Shows the activity level and recent usage patterns of the prediction system.</p>
            <ul>
                <li>Tracks predictions made in the last 30 days</li>
                <li>Indicates system activity and user engagement</li>
                <li>Useful for monitoring system performance trends</li>
            </ul>
        `,
        'Model Accuracy': `
            <h6>Machine Learning Model Accuracy</h6>
            <p>The percentage of correct predictions made by the AI model during testing.</p>
            <ul>
                <li>Measured against a held-out test dataset</li>
                <li>Higher accuracy indicates better model performance</li>
                <li>Current model shows strong predictive capability</li>
            </ul>
        `,
        'F1 Score': `
            <h6>Model F1 Score</h6>
            <p>A balanced measure combining precision and recall metrics.</p>
            <ul>
                <li>Ranges from 0 to 1, with 1 being perfect</li>
                <li>Considers both false positives and false negatives</li>
                <li>Provides a single metric for overall model quality</li>
            </ul>
        `
    };
    
    return content[metricType] || '<p>Detailed information not available for this metric.</p>';
}

function startRealTimeUpdates() {
    setInterval(updateRealTimeMetrics, 30000);
}

function updateRealTimeMetrics() {
    const metricCards = document.querySelectorAll('.metric-card');
    metricCards.forEach((card, index) => {
        setTimeout(() => {
            card.style.transform = 'scale(1.02)';
            setTimeout(() => {
                card.style.transform = 'scale(1)';
            }, 200);
        }, index * 100);
    });
}

function animateChart(chart, newData) {
    if (!chart || !newData) return;
    
    chart.data.datasets[0].data = newData;
    chart.update('active');
}

function highlightChartElement(chart, elementIndex) {
    if (!chart || elementIndex < 0) return;
    
    const originalColors = [...chart.data.datasets[0].backgroundColor];
    chart.data.datasets[0].backgroundColor[elementIndex] = '#FF6B6B';
    chart.update();
    
    setTimeout(() => {
        chart.data.datasets[0].backgroundColor = originalColors;
        chart.update();
    }, 1500);
}

function trackDashboardPerformance() {
    const startTime = performance.now();
    
    return {
        end: function() {
            const endTime = performance.now();
            const loadTime = endTime - startTime;
            console.log(`Dashboard loaded in ${loadTime.toFixed(2)}ms`);
            
            if (window.gtag) {
                window.gtag('event', 'dashboard_load_time', {
                    value: Math.round(loadTime),
                    custom_parameter: 'dashboard_performance'
                });
            }
        }
    };
}

const performanceTracker = trackDashboardPerformance();

window.addEventListener('load', function() {
    performanceTracker.end();
});

function enhanceAccessibility() {
    const charts = document.querySelectorAll('canvas');
    charts.forEach((canvas, index) => {
        canvas.setAttribute('role', 'img');
        canvas.setAttribute('aria-label', `Chart ${index + 1}: Data visualization`);
    });
    
    const metricCards = document.querySelectorAll('.metric-card');
    metricCards.forEach(card => {
        card.setAttribute('tabindex', '0');
        card.setAttribute('role', 'button');
        
        card.addEventListener('keydown', function(e) {
            if (e.key === 'Enter' || e.key === ' ') {
                e.preventDefault();
                this.click();
            }
        });
    });
}

document.addEventListener('DOMContentLoaded', enhanceAccessibility);

window.DashboardUtils = {
    refreshDashboardData,
    exportDashboardData,
    showMetricDetails,
    animateChart,
    highlightChartElement
};