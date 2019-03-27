import FWCore.ParameterSet.Config as cms

process = cms.Process("rpcNtupler")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = "93X_upgrade2023_realistic_v5"

from RecoLocalMuon.RPCRecHit.rpcRecHits_cfi import rpcRecHits
process.rpcRecHits = rpcRecHits

process.rpcRecHits.rpcDigiLabel = cms.InputTag("simMuonRPCDigis")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
#process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(10) )

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
       'file:/pnfs/knu.ac.kr/data/cms/store/user/jichoi/RPC+CSCTrigger/testoutput/rpcoutput-testone.root'
    )
)

process.rpcntupler = cms.EDAnalyzer("CSCExtrapoltoRPC",
   cscSegments = cms.InputTag('cscSegments'),
   tracks = cms.untracked.InputTag('tracks'),
#   rpcRecHits = cms.InputTag('rpcRecHits'),
#   simMuonRPCDigis = cms.InputTag('simMuonRPCDigis'),
   simMuonRPCDigis = cms.InputTag('rpcRecHits'),
   simCSCTriggerpreDigis = cms.InputTag('simCscTriggerPrimitiveDigis') 
)

process.TFileService = cms.Service("TFileService",
     fileName = cms.string('rpcNtuple.root')
 )

process.p = cms.Path(process.rpcntupler)
